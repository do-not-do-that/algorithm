# 트리 순회
# 항상 A 가 루트 노드가 됨.
# 재귀 사용하면 될듯?
# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}


def preorder(root):
    # print("root 확인 : ", root)
    if root != ".":
        print(root, end="")  # 자기 자신부터 출력
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


N = int(input())
tree = {}

# 부모 중심으로 트리 생성
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


# print("N : ", N)
# print("tree : ", tree)
preorder("A")
print()
inorder("A")
print()
postorder("A")
