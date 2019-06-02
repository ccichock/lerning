from Class_Name import Class_List


class Tag_Params_List:


    def __init__(self):
        self.class_names = Class_List()
        self.tag_params_list = dict()
        self.href = ''

    def add_class(self, class_name):
        self.class_names.add_class(class_name)

        class_string = f' class="{self.class_names.to_string()}"'
        self.tag_params_list.update({'class': class_string})


    def add_href(self, url):
        href_string = f' href="{url}"'
        self.tag_params_list.update({'href': href_string})


    def params_string(self):

        if self.tag_params_list:
            tag_params = ''.join(self.tag_params_list.values())
        else:
            tag_params = ''

        return tag_params