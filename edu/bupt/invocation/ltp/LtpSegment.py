# -*- coding: utf-8 -*-
import os
from pyltp import Segmentor, NamedEntityRecognizer
from pyltp import Postagger

LTP_DATA_DIR = './model/'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`


class LtpSegment:
    def __init__(self):
        print '初始化【segment model】...',
        self.segmentor = Segmentor()
        self.segmentor.load(cws_model_path)
        print '【segment model】初始化完成\n'
        print '初始化【实体识别model】...',
        self.recognizer = NamedEntityRecognizer()  # 初始化实例
        self.recognizer.load(ner_model_path)
        print '【实体识别model】初始化完成\n'
        print '初始化【词性标注model】...',
        self.pos_tag = Postagger()
        self.pos_tag.load(pos_model_path)
        print '【词性标注model】初始化完成\n'

    def segment(self, sentence):
        words = self.segmentor.segment(sentence)
        return words

    def postag(self, words):
        postags = self.pos_tag.postag(words)
        return postags

    def ner(self, words, postags):
        netags = self.recognizer.recognize(words, postags)
        return netags


if __name__ == '__main__':
    ltpSegment = LtpSegment()
    sentence = '深圳市腾讯计算机系统有限公司成立于1998年11月[1]  ，由马化腾、张志东、许晨晔、陈一丹、曾李青五位创始人共同创立。[1]  是中国最大的互联网综合服务提供商之一，也是中国服务用户最多的互联网企业之一。[2] '
    words = ltpSegment.segment(sentence)
    print ' '.join(words)
    postags = ltpSegment.postag(words)
    print ' '.join(postags)
    ners = ltpSegment.ner(words, postags)
    print ' '.join(ners)
