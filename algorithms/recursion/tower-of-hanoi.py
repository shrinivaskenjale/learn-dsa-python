def solve(n, source, destination, helper):
    # Base case: If there is only one disk, we can directly move it to destination from source without any worry.
    if n == 1:
        print("Move {} disk from {} to {}".format(n, source, destination))
        return

    # First move top n-1 disks to helper from source using destination
    solve(n - 1, source, helper, destination)
    # Move last 1 remaining disk from source to destination
    solve(1, source, destination, helper)
    # Finally, move n-1 disks moved to helper previously to distination using source.
    solve(n - 1, helper, destination, source)


n = 3
# Move n disks from source to destination with the help of helper.
solve(n, "source", "destination", "helper")
