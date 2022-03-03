class TreeNode:
  def __init__(self,data):
    self.data = data
    self.children = []
    self.parent = None

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level

  def add_child(self,child):
    child.parent = self
    self.children.append(child)

  def print_tree(self):
    spaces = ' ' * self.get_level() * 3
    print(spaces + '-' +self.data)
    if self.children:
      for i in self.children:
        i.print_tree()

def build_product_tree():
  root = TreeNode("Electronics")

  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Mac"))
  laptop.add_child(TreeNode("Thinkpad"))
  laptop.add_child(TreeNode("Windows"))

  cellphone = TreeNode("Cell Phone")
  cellphone.add_child(TreeNode("iphone"))
  cellphone.add_child(TreeNode("Lenevo"))
  cellphone.add_child(TreeNode("vivo"))

  tv = TreeNode("TV")
  tv.add_child(TreeNode("LG"))
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("Videocon"))

  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)

  return root

root = build_product_tree()
root.print_tree()
# print(root.get_level())
