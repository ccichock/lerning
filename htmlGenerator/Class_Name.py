

class Class_Name:
    def __init__(self, class_name):
        self.class_info = class_name.split('-')


    def type(self):
        return self.class_info[0]


    def value(self):
        return "-".join(self.class_info[1:])


    def set_value(self, value):
        values = value.split('-')
        
        new_class = [self.class_info[0]]
        new_class.extend(values)
        self.class_info = new_class


    def to_string(self):
        return "-".join(self.class_info)


class Class_List:
    def __init__(self):
        self.class_names = []


    def to_string(self):
        names = [class_name.to_string() for class_name in self.class_names]
        return " ".join(names)


    def find_class_name(self, to_find):
        to_find_class = Class_Name(to_find)

        class_names = [class_name for class_name in self.class_names if to_find_class.type() == class_name.type()]
        return class_names


    def add_class(self, to_add_classes):
        to_add_names = to_add_classes.split(' ')

        for to_add_name in to_add_names:

            to_modify = self.find_class_name(to_add_name)

            if not to_modify:
                self.class_names.append(Class_Name(to_add_name))
            else:
                to_add_class = Class_Name(to_add_name)
                to_add_value = to_add_class.value()
                to_modify[0].set_value(to_add_value)


    def remove_class(self, to_remove):
        pass