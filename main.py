# -*- coding: utf-8 -*-

class Responder:
    """ AIの応答を制御するクラス

    プロパティ
    name --Responderオブジェクトの名前
    """

    def __init__(self, name):
        self._name = name

    def response(self, text):
        return '{}ってなに?'.format(text)

    @property
    def name(self):
        return self._name

class Unmo:
    """人工無能コアクラス

    プロパティ：
        name: 人工無能コアの名前
        responder_name: 現在応答クラスの名前
    """

    def __init__(self, name):
        self._name = name
        self._responder = Responder('What')

    def dialogue(self, text):
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name

def build_prompt(unmo):
    return '{name}:{responder}> '.format(name = unmo.name, responder = unmo.responder_name)

if __name__ == '__main__':
    print('Unmo System Prototype : proto')
    proto = Unmo('proto')
    while True:
        text = input('> ')
        if not text:
            break

        response = proto.dialogue(text)
        print('{prompt}:{responder}'.format(prompt = build_prompt(proto), responder = response))

