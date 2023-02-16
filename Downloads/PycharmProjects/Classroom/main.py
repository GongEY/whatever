import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

batch_size = 125
test_size = 200
training_epochs = 20

mnist = input_data.read_data_sets("MNIST_DATA/", one_hot = True)

X = tf.placeholder("float", [None, 28, 28, 1])
Y = tf.placeholder("float", [None, 10])

W1 = tf.Variable(tf.random_normal(shape = [5, 5, 1, 4], stddev = 0.01))
L1 = tf.nn.conv2d(X, W1, strides = [1, 1, 1, 1], padding = 'SAME')
L1 = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')

W2 = tf.Variable(tf.random_normal(shape = [5, 5, 4, 12], stddev = 0.01))
L2 = tf.nn.conv2d(L1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
L2 = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')

L3 = tf.reshape(L2, [-1, 12*4*4])

W3 = tf.get_variable(name = "W3", shape = [12*4*4, 10], initializer = tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([10]))
hello = tf.matmul(L3, W3) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = hello, labels = Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = tf.argmax(hello, 1)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(training_epochs):
        avg_cost = 0
        avg_training_accuracy = 0
        total_batch = int(mnist.train.num_examples/batch_size)

        for step in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs_image = batch_xs.reshape(-1, 28, 28, 1)

            sess.run(train_op, feed_dict = {X: batch_xs_image, Y: batch_ys})
            avg_cost += sess.run(cost, feed_dict = {X: batch_xs_image, Y:batch_ys})/total_batch
            avg_training_accuracy += (np.mean(np.argmax(batch_ys, axis = 1) ==
                                    sess.run(predict_op, feed_dict={X: batch_xs_image,
                                                                    Y: batch_ys})))/total_batch
        print("Epoch: %d, training accuracy: %.4f" %(i, avg_training_accuracy))

        test_indices = np.arange(mnist.test.labels.shape[0])
        np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]
        teX = mnist.test.images[test_indices].reshape(-1, 28, 28, 1)

        testing_accuracy = np.mean(np.argmax(mnist.test.labels[test_indices], axis = 1) ==
                         sess.run(predict_op, feed_dict={X: teX, Y: mnist.test.labels[test_indices]}))
        print("Testing Accracy: %.4f" %(testing_accuracy))