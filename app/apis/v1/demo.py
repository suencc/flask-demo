import json


class Welcome:
    def __init__(self, name):
        self.name = name
        self.message = "Hello %s, Welcome to flask-restaction!" % name
        data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
        self.text = json.dumps(data)


class Hello:
    """
    Hello world
    $shared:
        user:
            id?int: Id
            age?int: 年龄 
        name:
            name?str&default="world": Your name
        message:
            message?str: Welcome message
    """

    def get(self, name):
        """
        Get welcome message

        $input:
            name?str&default="world": Your namesssss
        $output:
            message?str: Welcome message
            name?str: Welcome message
            text?str: Welcome message
        """

        me = Welcome
        me.name = "zxs"
        me.message = "mess"
        me.text = "aaa"

        data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
        print(json.dumps(data))

        return Welcome(name)

    def get_me(self):
        """
        Get welcome for me


        $output:
            name?str: Welcome message
            # data: ["&minlen=1&unique","int"]
            # data: ["&minlen=1",user@user: user]
            data: [@user]
            item:
                # user@user: user
                id?int: Id
                name?str: name
        """
        me = Welcome
        me.name = "zxs"
        me.message = "mess"
        me.text = "aaa"
        list = []
        list.append("zxs")
        list.append(100)
        list.append("xxx")
        user = {"id": 1, "name": "zxs", "age": 1}
        data = [user, user, user]
        idata = [1, 2, 3]
        item = {"id": 1, "name": "zxs", "age": 1, "user": user, "data": data}
        data = {"name": "zxs", "item": item, "age": 10, "data": data}
        return data
