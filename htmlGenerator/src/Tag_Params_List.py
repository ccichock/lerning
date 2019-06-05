from Class_Name import Class_List


class Tag_Params_List:

    def __init__(self):
        self.class_names = Class_List()
        self.tag_params_list = dict()
        self.href = ''


    def add_to_params_list(self, param, value):
        param_string = f' {param}="{value}"'
        self.tag_params_list.update({param: param_string})


    def add_class(self, class_name):
        self.class_names.add_class(class_name)
        self.add_to_params_list("class", self.class_names.to_string())


    def add_href(self, url):
        self.add_to_params_list("href", url)


    def add_placeholder(self, text):
        self.add_to_params_list("placeholder", text)


    def add_rel(self, text):
        self.add_to_params_list("rel", text)


    def add_integrity(self, text):
        self.add_to_params_list("integrity", text)


    def add_crossorigin(self, text):
        self.add_to_params_list("crossorigin", text)


    def add_src(self, src):
        self.add_to_params_list("src", src)


    def params_string(self):
        tag_params = ''

        if self.tag_params_list:
            tag_params = ''.join(self.tag_params_list.values())

        return tag_params