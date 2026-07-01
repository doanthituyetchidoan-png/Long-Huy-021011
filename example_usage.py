"""
Ví dụ cách sử dụng AI Chatbot trong code
"""

from ai_chatbot import SimpleChatBot

def example_basic_chat():
    """Ví dụ 1: Trò chuyện cơ bản"""
    print("\n=== Ví dụ 1: Trò chuyện cơ bản ===\n")
    
    bot = SimpleChatBot("LongHuy")
    
    questions = [
        "hello",
        "how are you",
        "what is your name",
        "thanks"
    ]
    
    for question in questions:
        response = bot.get_response(question)
        print(f"👤 Câu hỏi: {question}")
        print(f"🤖 Trả lời: {response}\n")


def example_custom_bot():
    """Ví dụ 2: Tạo bot tùy chỉnh"""
    print("\n=== Ví dụ 2: Bot tùy chỉnh ===\n")
    
    bot = SimpleChatBot("HuyBot Pro")
    
    # Thêm kiến thức tùy chỉnh
    bot.knowledge_base["python"] = [
        "Python là một ngôn ngữ lập trình rất mạnh!",
        "Tôi yêu thích Python vì nó đơn giản và dễ học."
    ]
    
    bot.knowledge_base["ai"] = [
        "AI (Artificial Intelligence) là tương lai!",
        "Machine Learning và Deep Learning rất thú vị."
    ]
    
    test_inputs = [
        "Tell me about python",
        "What about AI?",
        "I love coding"
    ]
    
    for user_input in test_inputs:
        response = bot.get_response(user_input)
        print(f"👤 {user_input}")
        print(f"🤖 {response}\n")


def example_conversation():
    """Ví dụ 3: Cuộc hội thoại đầy đủ"""
    print("\n=== Ví dụ 3: Cuộc hội thoại ===\n")
    
    bot = SimpleChatBot("ChatBot")
    
    conversation = [
        "Hi there!",
        "How are you?",
        "What's your name?",
        "That's cool!",
        "See you later!"
    ]
    
    for msg in conversation:
        response = bot.get_response(msg)
        print(f"👤 User: {msg}")
        print(f"🤖 {bot.name}: {response}\n")
    
    # In lịch sử
    print("\n" + "="*60)
    print("LỊCH SỬ CUỘC TRÒ CHUYỆN")
    print("="*60)
    bot.print_history()
    
    # Lưu lịch sử
    bot.save_history("example_history.json")


def example_stats():
    """Ví dụ 4: Thống kê cuộc trò chuyện"""
    print("\n=== Ví dụ 4: Thống kê ===\n")
    
    bot = SimpleChatBot("StatBot")
    
    # Mô phỏng cuộc trò chuyện
    messages = [
        "hello", "how are you", "what is your name",
        "hello again", "thanks", "bye"
    ]
    
    for msg in messages:
        bot.get_response(msg)
    
    history = bot.get_history()
    
    print(f"📊 Tổng số lần tương tác: {len(history)}")
    print(f"🤖 Bot: {bot.name}")
    print(f"📝 Lịch sử:")
    for i, chat in enumerate(history, 1):
        print(f"   {i}. Bạn: {chat['user']}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("    🤖 CÁC VÍ DỤ SỬ DỤNG AI CHATBOT")
    print("="*60)
    
    example_basic_chat()
    example_custom_bot()
    example_conversation()
    example_stats()
    
    print("\n" + "="*60)
    print("✓ Tất cả ví dụ đã chạy xong!")
    print("="*60 + "\n")
