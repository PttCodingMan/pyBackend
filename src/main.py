class Student:
    def ReadYaml(self, x, y):
        a = 10
        b = 'test'
        print(x)
        print(y)
        filePath = pathlib.Path(__file__).parent.absolute()
        print('%s is %s' % ('this filePath', filePath))

        yamlPath = str(filePath) + '/config/setting.yaml'

        # with open(r'E:\data\fruits.yaml') as file:
        with open(yamlPath) as file:
            fruits_list = yaml.load(file, Loader=yaml.FullLoader)
            print(fruits_list)


if __name__ == '__main__':
    import sys
    import pathlib
    import yaml
    import version

    # print("安安")
    s = Student()
    s.ReadYaml(3, 5)
    aa = version.V
    print(aa)
