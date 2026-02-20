def checkMessage(message):
    upper_count = 0
    punct_count = 0
    letter_count = 0
    is_spam = False
    repeating_count = 0
    prev_char = None
    msg_len = len(message)
    for i in range(msg_len):
        Current_char = message[i]
        # For detecting spam
        if Current_char == prev_char:
            repeating_count += 1
            if repeating_count > 3:  
                is_spam = True
        else:
            repeating_count = 1
            
        # for counting character types
        if Current_char.isalpha():
            letter_count += 1
            if Current_char.isupper():
                upper_count += 1
        elif Current_char in ['!', '?']:
            punct_count += 1
            
        # Updating previos character to the currrent one we have
        prev_char = Current_char

    #Caps Ratio
    caps_ratio = 0.0
    if letter_count > 0:
        caps_ratio = upper_count / letter_count

    # Determine Sentiment
    final_sentiment = "CALM"
    if caps_ratio >= 0.6 or punct_count >= 5:
        final_sentiment = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punct_count >= 3:
        final_sentiment = "URGENT"
    return final_sentiment, is_spam

#Testing the Exammples

# Test 1
msg1 = "Hey, want to connect?"
sentiment1, spam1 = checkMessage(msg1)
print("Message: ", msg1)
print("Sentiment: ", sentiment1, "| Spam: ", spam1)
print()  

# example 2
msg2 = "PLEASE ACCEPT MY REQUEST!!!"
sentiment2, spam2 = checkMessage(msg2)
print("Message: ", msg2)
print("Sentiment: ", sentiment2, "| Spam: ", spam2)
print()

# example 3
msg3 = "Are you free? I need to talk!!!"
sentiment3, spam3 = checkMessage(msg3)
print("Message: ", msg3)
print("Sentiment: ", sentiment3, "| Spam: ", spam3)
print()

# example 4
msg4 = "heyyyyy, what's up?"
sentiment4, spam4 = checkMessage(msg4)
print("Message: ", msg4)
print("Sentiment: ", sentiment4, "| Spam: ", spam4)
print()
