def pre_order(in_order, post_order, root):
    print(root, end=" ")
    if len(in_order) == 1:
        return
    elif len(in_order) == 2:
        print(post_order[0], end=" ")
        return
    if in_order[0] == post_order[-1]:
        pre_order(in_order[1:], post_order[:-1], post_order[-2])
    elif in_order[-1] == post_order[-1]:
        pre_order(in_order[:-1], post_order[:-1], post_order[-2])
    else:
        left_post_root_idx = post_order.index(in_order[in_order.index(root) + 1]) - 1
        pre_order(in_order[:in_order.index(root)], post_order[:left_post_root_idx + 1], post_order[left_post_root_idx])
        pre_order(in_order[in_order.index(root) + 1:], post_order[left_post_root_idx + 1:-1], post_order[-2])


N = map(int, input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pre_order(in_order, post_order, post_order[-1])