class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Count how many times each word should appear
        target = {}

        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        # Try every possible starting offset
        for start in range(word_len):

            left = start
            right = start
            current = {}
            count = 0

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                if word in target:
                    current[word] = current.get(word, 0) + 1
                    count += 1

                    # Too many copies of this word
                    while current[word] > target[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Found all words
                    if count == word_count:
                        result.append(left)

                        # Move forward for next possible match
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Word is not in the list
                    current.clear()
                    count = 0
                    left = right

        return result