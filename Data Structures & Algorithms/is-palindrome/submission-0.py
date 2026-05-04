class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_list = []

        for i in s:
            check_list.append(i)

        cleaned_check_list = [item.lower() for item in check_list if item.isalnum()]

        if cleaned_check_list == cleaned_check_list[::-1]:
            return True
        else:
            return False