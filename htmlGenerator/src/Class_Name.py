

class Class_Name:
    def __init__(self, class_name):
        self.class_info = class_name.split('-')


    def type(self):
        return self.class_info[0]


    def to_string(self):
        return "-".join(self.class_info)


class Class_List:
    def __init__(self):
        self.class_names = dict()


    def is_empty(self):
        return not self.class_names


    def to_string(self):
        values = list()

        for value in self.class_names.values():
            values.extend(value)

        return " ".join(values)


    def add_class(self, to_add_classes):
        if to_add_classes:
            to_add_names = to_add_classes.split(' ')

            for to_add_name in to_add_names:
                to_add = Class_Name(to_add_name)
                if not to_add.type() in self.class_names:
                    self.class_names.update({to_add.type() : [to_add.to_string()]})
                else:
                    type_value_list = self.class_names[to_add.type()]
                    type_value_list.append(to_add.to_string())


    def remove_class(self, to_remove_classes):
        to_remove_names = to_remove_classes.split(' ')

        for to_remove_name in to_remove_names:
            to_remove = Class_Name(to_remove_name)
            self.class_names.pop(to_remove.type())