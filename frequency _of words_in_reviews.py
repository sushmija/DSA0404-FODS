import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Sample data (replace this with your actual customer reviews dataset)
customer_reviews = [
    "The product is excellent and worth the money.",
    "I'm not satisfied with the quality.",
    "Great value for the price!",
    # ... more reviews ...
]

# Combine all reviews into a single string
all_reviews_text = ' '.join(customer_reviews)

# Tokenize the text into words
words = word_tokenize(all_reviews_text)

# Calculate the frequency distribution of words
freq_dist = FreqDist(words)

# Display the most common words and their frequencies
print("Top 10 Most Common Words:")
print(freq_dist.most_common(10))

# Plot the frequency distribution
plt.figure(figsize=(10, 6))
freq_dist.plot(30, cumulative=False)
plt.title("Word Frequency Distribution in Customer Reviews")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
