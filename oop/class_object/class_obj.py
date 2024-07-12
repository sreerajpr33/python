# class syneffo:
#     def python():
#         print('python in syn')
#     def php():
#         print('php')
# s=syneffo
# s.python()
# s.php()
# r=syneffo
# r.python()


class syneffo:
    def python(s):
        s.database='mysql'
        print('python')
    def php(self):
        print('php',self.database)
s=syneffo()
s.python()
print(s.database)
s.php()
