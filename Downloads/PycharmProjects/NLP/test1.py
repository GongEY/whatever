import kr.bydelta.koala.twt.SentenceSplitter

#새 문장분리기를 초기화합니다.
val sentSplit = new SentenceSplitter
#분리할 문장
val paragraph = "누군가가 말했다. Python에는 KoNLPy가 있다. Scala는 KoalaNLP가 있었다."
#문장들로 분리합니다.
val sentences: Seq[String] = sentSplit.sentences(paragraph)