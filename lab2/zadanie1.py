from functools import reduce
import string
text ="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus massa eros, iaculis quis sapien non, placerat convallis neque. Cras dui lectus, pretium sit amet quam quis, varius aliquam quam. Donec in nulla eu quam pharetra feugiat et ut nisi. Phasellus suscipit euismod lectus nec imperdiet. Praesent in malesuada diam, vitae euismod libero. Maecenas turpis lectus, finibus at orci a, lobortis tincidunt enim. Etiam maximus erat ipsum, et lobortis purus pulvinar eget.
Nam hendrerit est quis ante dignissim, eget semper dui gravida. Integer efficitur imperdiet rutrum. Integer fermentum vel elit eu ultricies. Curabitur tortor lectus, finibus ut pulvinar sit amet, lobortis sit amet mi. Aenean et mi mollis, viverra nibh quis, fringilla mi. Vestibulum ex elit, aliquet id libero id, volutpat mollis nisl. Nunc suscipit ante vitae quam suscipit, quis molestie nisl blandit.
Pellentesque in pretium velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Quisque finibus tempor elit. Vivamus augue sem, dignissim sit amet laoreet tempus, scelerisque quis orci. Fusce et lacus nibh. Nunc sagittis odio libero, eget hendrerit orci volutpat in. Vivamus et tempor ligula. Curabitur diam arcu, pellentesque non tellus quis, euismod tempus est. Donec vitae tempor lorem. In non eleifend diam, vitae rhoncus arcu. Praesent ac massa ex.
Nullam lorem ipsum, auctor mattis congue ut, suscipit sit amet nulla. Fusce laoreet sapien in mi iaculis, sed convallis metus faucibus. Etiam eu dignissim arcu. Nullam eu nibh laoreet, semper quam tristique, tempus arcu. Nam et mattis ante. Duis sollicitudin sem eget nisl molestie semper. Donec at nunc eget ipsum volutpat posuere eget vitae massa. Vivamus pellentesque eros tortor, et aliquam ligula dapibus a. Nullam pharetra tristique felis tempus feugiat. Nunc cursus tincidunt erat.
Ut id posuere odio. Praesent vel justo tempor orci dapibus bibendum id ut justo. Duis velit turpis, suscipit sed urna at, tempor laoreet arcu. Nunc id risus et nibh vehicula tincidunt at scelerisque tortor. Nulla tempus quam porta enim molestie laoreet sed eu turpis. Quisque dapibus nisl est, a hendrerit est tincidunt ut. Morbi tincidunt facilisis sapien, eu commodo erat suscipit vitae. Vestibulum quis ipsum nec felis iaculis posuere. Sed eu nisl ac turpis elementum posuere ac a neque. Pellentesque vulputate dapibus porttitor. Donec finibus libero vitae ante sagittis accumsan. Cras eget semper turpis. Nam volutpat nunc id tellus imperdiet, nec pretium tortor maximus. Integer condimentum tellus augue, vel tincidunt massa pretium sit amet. Quisque egestas enim metus, placerat vulputate dui pharetra at.
"""
stopWords = {"i", "a", "the", "to", "of", "and", "in", "on", "for", "with", "at"}
#lepiej było by użyć split'a
def amounts(text): 
    return {
        'paragraphs': len([x for x in text if x == "\n"]),
        'sentences': len([x for x in text if x in [".", "!", "?"]]),
        'words': len([x for x in text if x == " "])+1
    }
def mostFrequentWord(text):
    translator = str.maketrans('', '', string.punctuation)
    words = [word.translate(translator).lower() for word in text.split()]
    filteredWords = [word for word in words if word not in stopWords]
    wordCount = reduce(lambda acc, word: {**acc, word: acc[word]+1 if word in acc else 1}, filteredWords, {})
    return [max(wordCount, key=wordCount.get), wordCount[max(wordCount, key=wordCount.get)]]

def reverseWords(text):
    #możemy to zrobić bo text - argument a nie zmienna
    words = text.split()
    def reverseWord(word):
        if word[0].lower() == 'a':
            return word[::-1]
        return word
    transformed_words = map(reverseWord, words)
    return ' '.join(transformed_words)


print(amounts(text)['paragraphs'])
print(amounts(text)['sentences'])
print(amounts(text)['words'])

print(reverseWords(text))


print(mostFrequentWord(text))