import re


class Poem(object):
    poem_cnt = 0

    def __init__(self, json_data=None):
        self.id = Poem.poem_cnt
        Poem.poem_cnt += 1
        if json_data is None:
            raise NotImplementedError
        else:
            self.title = json_data['name']
            self.author = json_data['author']
            self.dynasty = json_data['dynasty']
            content = json_data['poem']
            content = re.split('，|。|；|？|、|·|…|（|）|/|《|》|“|”|‘|’', content)
            content = [element for element in filter(
                lambda x:x != "", content)]
            self.content = content

    def __str__(self):
        ret = ""
        ret = ret + "id:\t" + str(self.id) + "\n"
        ret = ret + "title:\t" + str(self.title) + "\n"
        ret = ret + "author:\t" + str(self.author) + "\n"
        ret = ret + "content:\t" + str(" ".join(self.content)) + "\n"
        return ret

    def pace(self):
        ret = []
        for line in self.content:
            ret.append(len(line))
        return tuple(ret)
