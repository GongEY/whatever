from tensorflow.examples.tutorials.mnist import input_data

# load mnist datasets
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

print(tf.convert_to_tensor(mnist.train.images).get_shape())
print(tf.convert_to_tensor(mnist.train.labels).get_shape())

# set variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# placeholder for input data
x = tf.placeholder("float", [None, 784])
y_ = tf.placeholder("float", [None, 10])

# build softmax model
y = tf.nn.softmax(tf.matmul(x, W) + b)

# loss function
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# optimization
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

for step in range(1000):
    # get 100 images for each iteration
    batch_xs, batch_ys = mnist.train.next_batch(100)

    # train the model
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # test the results
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images,
                                              y_: mnist.test.labels})

    print('step: {:01d} | accuracy : {:.4f}'.format(step, float(accuracy_)))








