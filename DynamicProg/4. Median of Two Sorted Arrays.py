def binary(value, array):
    a, b = 0, len(array) - 1
    while b - a > 1:
        c = a + (b - a) // 2
        if array[c] < value:
            a = c
        else:
            b = c
    return b


class ShortenedList(list):
    def __init__(self, *args, **kwargs):
        self.l = 0
        self.r = 0
        self.array = args[0]
        super(ShortenedList, self).__init__(*args, **kwargs)

    def i(self, i):
        return self.array[i + self.l]

    def len(self):
        return len(self.array) - self.l - self.r

    def crop(self, v):
        if v > 0:
            self.l += v
        else:
            self.r -= v

    def _1_median(self):
        return [self.i(self.len()//2), self.i(self.len()//2-1)]

    def __repr__(self):
        return f"{self.array[self.l:len(self.array)-self.r]} :: {self.array} {self.l} {self.r}"


def get_median(arr1, arr2):
    if arr1.len() == 1 or arr2.len() == 1:
        return arr1, arr2

    m1 = arr1.len()//2
    m2 = arr2.len()//2
    m = min(m1, m2)
    a = arr1.i(m1)
    b = arr2.i(m2)
    if b > a:
        arr1.crop(m)
        arr2.crop(-m)
        return get_median(arr2, arr1)
    arr1.crop(-m)
    arr2.crop(m)
    return get_median(arr1, arr2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        c = (n + m) //2

        arr1, arr2 = get_median(ShortenedList(nums1), ShortenedList(nums2))
        if arr2.len() == 1 and arr2.len() == 1:
            if arr1.i(0) > arr2.i(0):
                arr1, arr2 = arr2, arr1
            d = arr2.i(-1)
            if d > arr1.i(0):
                return (arr2.i(0)+d)/2
            return (arr1.i(0)+arr2.i(0))/2
        else:
            med = arr2.median()
            if arr2.len() % 2 == 1:
                a, b, c = arr2.i(arr2.len()//2-1), arr2.i(arr2.len()//2), arr2.i(arr2.len()//2+1)
                if med < a:
                    return (a+b)/2
                if med > c:
                    return (b+c)/2
                return (med+c)/2

            else:
                a, b = arr2.i(arr2.len()//2-1), arr2.i(arr2.len()//2)
                if arr1.i(0) < a: return a
                if arr1.i(0) > b: return b
                return arr1.i(0)


print(Solution.findMedianSortedArrays(None, [1, 2], [3, 4]))# [-3, -2, -1, 1, 2, 3, 5, 7, 8], [-100, 4, 6, 10, 11, 12, 13, 14, 15]))
# [5, 6, 8, 11], [1, 2, 3, 4, 7, 9, 10]
#[5, 6, 8, 11, 12], [1, 2, 3, 4, 5.5, 7, 9, 10]))
