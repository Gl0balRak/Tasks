class FrequencyTracker(object):
    def __init__(self):
        self.nums = {}
        self.freq = {}

    def add(self, n):
        if n in self.nums.keys():
            self.freq[self.nums[n]] = self.freq[self.nums[n]] - 1
        self.nums[n] = self.nums.setdefault(n, 0) + 1
        self.freq[self.nums[n]] = self.freq.setdefault(self.nums[n], 0) + 1

    def deleteOne(self, n):
        if n in self.nums.keys():
            self.freq[self.nums[n]] = self.freq[self.nums[n]] - 1
        self.nums[n] = self.nums.setdefault(n, 1) - 1
        self.freq[self.nums[n]] = self.freq.setdefault(self.nums[n], 0) + 1

    def hasFrequency(self, f):
        return bool(self.freq.setdefault(f, 0) != 0)

ft = FrequencyTracker()
print(ft.freq, ft.nums)
ft.add(5)
print(ft.freq, ft.nums)
ft.add(4)
print(ft.freq, ft.nums)
ft.deleteOne(6)
print(ft.freq, ft.nums)
ft.deleteOne(4)
print(ft.freq, ft.nums)
ft.deleteOne(7)
print(ft.freq, ft.nums)
print(ft.hasFrequency(1))