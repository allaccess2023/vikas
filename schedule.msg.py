import asyncio
import datetime
from telegram import Bot
import aiohttp

# Replace with your Telegram bot token
bot_token = 'token'

# Replace with your group chat ID (you can get this from the @userinfobot)
chat_id = <group id>

# Initialize the bot
bot = Bot(token=bot_token)

# Function to send a message to the group
async def send_scheduled_message(bot, message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Error sending message: {e}")

# Define the scheduled messages with specific date and time
scheduled_messages = [
{"message": "Healthy Meal Ideas: Prepare homemade soups with plenty of vegetables for a nutrient-packed meal.", "date": "2023-11-11", "time": "13:00"},
{"message": "Healthy Meal Ideas: Grill, bake, or steam foods instead of frying for a healthier cooking method.", "date": "2023-11-12", "time": "13:00"},
{"message": "Healthy Meal Ideas: Plan meals ahead to avoid impulsive, unhealthy choices.", "date": "2023-11-13", "time": "13:00"},
{"message": "Healthy Meal Ideas: Avoid sugary drinks and opt for water, herbal tea, or infused water.", "date": "2023-11-14", "time": "13:00"},
{"message": "Healthy Meal Ideas: Enjoy healthy fats like avocados, nuts, and olive oil in moderation.", "date": "2023-11-15", "time": "13:00"},
{"message": "Healthy Meal Ideas: Make salads exciting with a variety of toppings like nuts, seeds, and fruits.", "date": "2023-11-16", "time": "13:00"},
{"message": "Healthy Meal Ideas: Control portion sizes to prevent overeating.", "date": "2023-11-17", "time": "13:00"},
{"message": "Healthy Meal Ideas: Limit processed foods and opt for whole, unprocessed options.", "date": "2023-11-18", "time": "13:00"},
{"message": "Healthy Meal Ideas: Include dairy or dairy alternatives for calcium and vitamin D.", "date": "2023-11-19", "time": "13:00"},
{"message": "Healthy Meal Ideas: Prepare stir-fries with a mix of veggies, lean protein, and a light sauce.", "date": "2023-11-20", "time": "13:00"},
{"message": "Healthy Meal Ideas: Snack on Greek yogurt with honey and berries for a protein-rich treat.", "date": "2023-11-21", "time": "13:00"},
{"message": "Healthy Meal Ideas: Substitute cauliflower or zucchini for some of the carbs in your favorite dishes.", "date": "2023-11-22", "time": "13:00"},
{"message": "Healthy Meal Ideas: Practice mindful eating by savoring each bite and eating without distractions.", "date": "2023-11-23", "time": "13:00"},
{"message": "Healthy Meal Ideas: Enjoy a balanced breakfast with protein, whole grains, and fruit.", "date": "2023-11-24", "time": "13:00"},
{"message": "Healthy Meal Ideas: Bake sweet potatoes instead of white potatoes for extra vitamins and fiber.", "date": "2023-11-25", "time": "13:00"},
{"message": "Healthy Meal Ideas: Try overnight oats with almond milk, chia seeds, and fresh fruit for breakfast.", "date": "2023-11-26", "time": "13:00"},
{"message": "Healthy Meal Ideas: Use nut butter as a dip for apple slices or celery.", "date": "2023-11-27", "time": "13:00"},
{"message": "Healthy Meal Ideas: Roast vegetables with olive oil and herbs for a tasty side dish.", "date": "2023-11-28", "time": "13:00"},
{"message": "Healthy Meal Ideas: Prepare a veggie-packed omelet for a protein-rich breakfast or brunch.", "date": "2023-11-29", "time": "13:00"},
{"message": "Healthy Meal Ideas: Experiment with different whole grain pasta options like quinoa or spelt.", "date": "2023-11-30", "time": "13:00"},
{"message": "Healthy Meal Ideas: Make your own smoothies with spinach, banana, and protein powder.", "date": "2023-12-01", "time": "13:00"},
{"message": "Healthy Meal Ideas: Go for lean cuts of meat to reduce saturated fat intake.", "date": "2023-12-02", "time": "13:00"},
{"message": "Healthy Meal Ideas: Snack on air-popped popcorn with a sprinkle of nutritional yeast.", "date": "2023-12-03", "time": "13:00"},
{"message": "Healthy Meal Ideas: Make a homemade vegetable pizza with whole wheat crust and lots of veggies.", "date": "2023-12-04", "time": "13:00"},
{"message": "Healthy Meal Ideas: Limit added sugars and choose fruit for natural sweetness.", "date": "2023-12-05", "time": "13:00"},
{"message": "Healthy Meal Ideas: Incorporate flaxseeds or chia seeds into your morning yogurt or oatmeal.", "date": "2023-12-06", "time": "13:00"},
{"message": "Healthy Meal Ideas: Cook with garlic and onions for added flavor and health benefits.", "date": "2023-12-07", "time": "13:00"},
{"message": "Healthy Meal Ideas: Swap sugary cereals for whole grain options with low sugar content.", "date": "2023-12-08", "time": "13:00"},
{"message": "Healthy Meal Ideas: Prepare a satisfying grain bowl with quinoa, roasted veggies, and a protein source.", "date": "2023-12-09", "time": "13:00"},
{"message": "Healthy Meal Ideas: Choose whole fruits over fruit juices for more fiber and fewer sugars.", "date": "2023-12-10", "time": "13:00"},
{"message": "Healthy Meal Ideas: Make a hearty chili with beans, lean meat, and plenty of spices.", "date": "2023-12-11", "time": "13:00"},
{"message": "Healthy Meal Ideas: Use avocado as a creamy spread on sandwiches and wraps.", "date": "2023-12-12", "time": "13:00"},
{"message": "Healthy Meal Ideas: Experiment with international cuisines to discover new, healthy recipes.", "date": "2023-12-13", "time": "13:00"},
{"message": "Healthy Meal Ideas: Limit high-calorie toppings on salads like croutons and heavy dressings.", "date": "2023-12-14", "time": "13:00"},
{"message": "Healthy Meal Ideas: Snack on unsalted mixed nuts for a dose of healthy fats and protein.", "date": "2023-12-15", "time": "13:00"},
{"message": "Healthy Meal Ideas: Create a balanced plate with one-half vegetables, one-quarter lean protein, and one-quarter whole grains.", "date": "2023-12-16", "time": "13:00"},
{"message": "Healthy Meal Ideas: Blend frozen bananas for a dairy-free ice cream alternative.", "date": "2023-12-17", "time": "13:00"},
{"message": "Healthy Meal Ideas: Prepare a colorful fruit salad with a variety of seasonal fruits.", "date": "2023-12-18", "time": "13:00"},
{"message": "Healthy Meal Ideas: Choose whole wheat bread over white bread for added fiber.", "date": "2023-12-19", "time": "13:00"},
{"message": "Healthy Meal Ideas: Make a simple, homemade tomato sauce for pasta with fresh herbs.", "date": "2023-12-20", "time": "13:00"},
{"message": "Healthy Meal Ideas: Substitute cauliflower rice for regular rice in stir-fries or Mexican dishes.", "date": "2023-12-21", "time": "13:00"},
{"message": "Healthy Meal Ideas: Roast or grill fish with lemon and herbs for a quick, healthy meal.", "date": "2023-12-22", "time": "13:00"},
{"message": "Healthy Meal Ideas: Eat slowly to give your brain time to recognize fullness.", "date": "2023-12-23", "time": "13:00"},
{"message": "Healthy Meal Ideas: Mix quinoa with black beans, corn, and salsa for a tasty salad.", "date": "2023-12-24", "time": "13:00"},
{"message": "Healthy Meal Ideas: Keep a food diary to track your eating habits and make healthier choices.", "date": "2023-12-25", "time": "13:00"},
{"message": "Healthy Snack Suggestions: Try air-fried sweet potato fries with a pinch of sea salt.", "date": "2023-11-11", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Combine cottage cheese with fresh pineapple for a protein-packed treat.", "date": "2023-11-12", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Create a trail mix with dried fruit, nuts, and seeds.", "date": "2023-11-13", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on rice cakes topped with avocado and sliced tomato.", "date": "2023-11-14", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Slice cucumbers and sprinkle with Tajin seasoning for a zesty snack.", "date": "2023-11-15", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Bake your own kale chips with olive oil and a touch of sea salt.", "date": "2023-11-16", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Make a smoothie bowl with your favorite toppings like granola and berries.", "date": "2023-11-17", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on edamame for a protein-rich, plant-based option.", "date": "2023-11-18", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Pop your own popcorn on the stove for a healthy, whole-grain snack.", "date": "2023-11-19", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Slice a banana and spread almond butter for a satisfying snack.", "date": "2023-11-20", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Mix low-fat cottage cheese with salsa for a protein-packed dip.", "date": "2023-11-21", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Choose a handful of cherry tomatoes as a low-calorie snack.", "date": "2023-11-22", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Keep pre-cut vegetables like bell peppers and broccoli in the fridge for quick snacking.", "date": "2023-11-23", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Make a fruit salad with a variety of berries and a drizzle of lemon juice.", "date": "2023-11-24", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Spread whole-grain crackers with avocado and a sprinkle of sea salt.", "date": "2023-11-25", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on plain, unsalted rice cakes for a low-calorie option.", "date": "2023-11-26", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Have a hard-boiled egg for a portable source of protein.", "date": "2023-11-27", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Savor a small piece of dark chocolate for a sweet, antioxidant-rich indulgence.", "date": "2023-11-28", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Mix diced mango with lime juice and a touch of chili powder for a flavorful snack.", "date": "2023-11-29", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Enjoy a small bowl of mixed berries for a low-calorie treat.", "date": "2023-11-30", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on seaweed snacks for a crunchy, low-calorie option.", "date": "2023-12-01", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Dip apple slices in natural peanut butter for a balance of protein and fiber.", "date": "2023-12-02", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Choose low-fat string cheese as a convenient, portion-controlled snack.", "date": "2023-12-03", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Have a cup of vegetable soup for a warm and satisfying snack.", "date": "2023-12-04", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on a small handful of grapes for a burst of natural sweetness.", "date": "2023-12-05", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Make your own fruit kabobs with a variety of fresh fruit chunks.", "date": "2023-12-06", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Blend frozen bananas into a creamy, dairy-free `nice cream.`", "date": "2023-12-07", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Opt for unsweetened, plain yogurt and add your favorite toppings.", "date": "2023-12-08", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Create a mini caprese salad with cherry tomatoes, mozzarella, and fresh basil.", "date": "2023-12-09", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Keep a container of mixed, unsalted nuts for an easy grab-and-go snack.", "date": "2023-12-10", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on whole grain crackers with low-sodium, nitrate-free turkey slices.", "date": "2023-12-11", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Make your own guacamole with mashed avocado, tomatoes, and lime juice.", "date": "2023-12-12", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Enjoy a small bowl of fresh melon cubes for a hydrating snack.", "date": "2023-12-13", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Sip on a homemade green smoothie with spinach, banana, and almond milk.", "date": "2023-12-14", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on sliced bell peppers with a light vinaigrette for dipping.", "date": "2023-12-15", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Top celery sticks with a dollop of cream cheese and chives.", "date": "2023-12-16", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Prepare a bowl of oatmeal with almond butter and sliced banana.", "date": "2023-12-17", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Have a cup of warm herbal tea with a slice of lemon.", "date": "2023-12-18", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on a small portion of whole grain, low-sugar cereal with milk.", "date": "2023-12-19", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Slice cucumber into thin rounds and top with smoked salmon.", "date": "2023-12-20", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Make your own energy bites with oats, honey, nuts, and dried fruit.", "date": "2023-12-21", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Savor a small serving of whole grain, low-fat granola with Greek yogurt.", "date": "2023-12-22", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Try baked apple chips with a sprinkle of cinnamon for a healthy crunch.", "date": "2023-12-23", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Snack on a handful of dried seaweed for a unique taste and texture.", "date": "2023-12-24", "time": "14:00"},
{"message": "Healthy Snack Suggestions: Create a mini sandwich with whole wheat bread, turkey, and mustard for a savory snack.", "date": "2023-12-25", "time": "14:00"},
{"message": "Workouts Tips: Include balance and flexibility exercises like yoga or Pilates.", "date": "2023-11-11", "time": "15:00"},
{"message": "Workouts Tips: Set specific, achievable fitness goals to stay motivated.", "date": "2023-11-12", "time": "15:00"},
{"message": "Workouts Tips: Make time for stretching to improve flexibility and reduce muscle soreness.", "date": "2023-11-13", "time": "15:00"},
{"message": "Workouts Tips: Gradually increase the intensity and duration of your workouts.", "date": "2023-11-14", "time": "15:00"},
{"message": "Workouts Tips: Monitor your heart rate during cardio to ensure you're in your target zone.", "date": "2023-11-15", "time": "15:00"},
{"message": "Workouts Tips: Try high-intensity interval training (HIIT) for efficient calorie burning.", "date": "2023-11-16", "time": "15:00"},
{"message": "Workouts Tips: Invest in comfortable workout attire and supportive shoes.", "date": "2023-11-17", "time": "15:00"},
{"message": "Workouts Tips: Stay hydrated throughout your workout to prevent dehydration.", "date": "2023-11-18", "time": "15:00"},
{"message": "Workouts Tips: Alternate between different muscle groups to prevent overtraining.", "date": "2023-11-19", "time": "15:00"},
{"message": "Workouts Tips: Use resistance bands or free weights to build muscle strength.", "date": "2023-11-20", "time": "15:00"},
{"message": "Workouts Tips: Listen to music or podcasts to stay entertained during workouts.", "date": "2023-11-21", "time": "15:00"},
{"message": "Workouts Tips: Include rest days to allow your body to recover and repair.", "date": "2023-11-22", "time": "15:00"},
{"message": "Workouts Tips: Perform core-strengthening exercises like planks and bicycle crunches.", "date": "2023-11-23", "time": "15:00"},
{"message": "Workouts Tips: Join a fitness class or group to stay engaged and socialize.", "date": "2023-11-24", "time": "15:00"},
{"message": "Workouts Tips: Track your progress to see improvements and adjust your routine.", "date": "2023-11-25", "time": "15:00"},
{"message": "Workouts Tips: Get outdoors for activities like hiking, biking, or running.", "date": "2023-11-26", "time": "15:00"},
{"message": "Workouts Tips: Make time for a cool-down to lower your heart rate and reduce muscle tension.", "date": "2023-11-27", "time": "15:00"},
{"message": "Workouts Tips: Consult a fitness professional for personalized guidance.", "date": "2023-11-28", "time": "15:00"},
{"message": "Workouts Tips: Practice deep breathing to reduce stress during workouts.", "date": "2023-11-29", "time": "15:00"},
{"message": "Workouts Tips: Explore different sports or recreational activities for a fun workout.", "date": "2023-11-30", "time": "15:00"},
{"message": "Workouts Tips: Challenge yourself with progressive overload, increasing weights or resistance.", "date": "2023-12-01", "time": "15:00"},
{"message": "Workouts Tips: Use a fitness app or tracker to monitor your workouts and progress.", "date": "2023-12-02", "time": "15:00"},
{"message": "Workouts Tips: Stay consistent with your exercise routine for long-term results.", "date": "2023-12-03", "time": "15:00"},
{"message": "Workouts Tips: Incorporate interval training to boost metabolism and burn fat.", "date": "2023-12-04", "time": "15:00"},
{"message": "Workouts Tips: Invest in home workout equipment like dumbbells or resistance bands.", "date": "2023-12-05", "time": "15:00"},
{"message": "Workouts Tips: Schedule your workouts in advance to prioritize fitness.", "date": "2023-12-06", "time": "15:00"},
{"message": "Workouts Tips: Include exercises that target your trouble areas.", "date": "2023-12-07", "time": "15:00"},
{"message": "Workouts Tips: Stay mindful of your body's signals and avoid overexertion.", "date": "2023-12-08", "time": "15:00"},
{"message": "Workouts Tips: Try yoga or meditation for stress relief and flexibility.", "date": "2023-12-09", "time": "15:00"},
{"message": "Workouts Tips: Change up your routine regularly to prevent boredom and plateaus.", "date": "2023-12-10", "time": "15:00"},
{"message": "Workouts Tips: Focus on compound movements that work multiple muscle groups.", "date": "2023-12-11", "time": "15:00"},
{"message": "Workouts Tips: Engage in activities you enjoy to make exercise a habit.", "date": "2023-12-12", "time": "15:00"},
{"message": "Workouts Tips: Take advantage of online workout tutorials and classes.", "date": "2023-12-13", "time": "15:00"},
{"message": "Workouts Tips: Use a fitness journal to track your workouts and nutrition.", "date": "2023-12-14", "time": "15:00"},
{"message": "Workouts Tips: Stay patient; results may take time, but consistency is key.", "date": "2023-12-15", "time": "15:00"},
{"message": "Workouts Tips: Mix in high- and low-impact exercises to cater to your fitness level.", "date": "2023-12-16", "time": "15:00"},
{"message": "Workouts Tips: Vary your training intensity for improved cardiovascular health.", "date": "2023-12-17", "time": "15:00"},
{"message": "Workouts Tips: Incorporate body measurements in addition to weight as a progress marker.", "date": "2023-12-18", "time": "15:00"},
{"message": "Workouts Tips: Join a sports league or team for a social workout experience.", "date": "2023-12-19", "time": "15:00"},
{"message": "Workouts Tips: Stay mindful of your posture during strength training exercises.", "date": "2023-12-20", "time": "15:00"},
{"message": "Workouts Tips: Seek guidance from a personal trainer for custom workouts.", "date": "2023-12-21", "time": "15:00"},
{"message": "Workouts Tips: Explore different types of dance for a fun and cardio-intensive workout.", "date": "2023-12-22", "time": "15:00"},
{"message": "Workouts Tips: Perform exercises that improve functional strength and balance.", "date": "2023-12-23", "time": "15:00"},
{"message": "Workouts Tips: Engage in active recovery on rest days, like walking or light yoga.", "date": "2023-12-24", "time": "15:00"},
{"message": "Workouts Tips: Celebrate your fitness milestones and reward yourself for achievements.", "date": "2023-12-25", "time": "15:00"},
{"message": "Workouts Tips: Prioritize getting enough sleep to aid recovery and muscle growth.", "date": "2023-12-26", "time": "15:00"},
{"message": "Workouts Tips: Experiment with different workout schedules to find what works for you.", "date": "2023-12-27", "time": "15:00"},
{"message": "Workouts Tips: Stay consistent with your nutrition to support your fitness goals.", "date": "2023-12-28", "time": "15:00"},
{"message": "Workouts Tips: Avoid excessive cardio that might lead to muscle loss.", "date": "2023-12-29", "time": "15:00"},
{"message": "Workouts Tips: Utilize online fitness communities for support and motivation.", "date": "2023-12-30", "time": "15:00"},
{"message": "Workouts Tips: Incorporate resistance training to increase metabolism.", "date": "2023-12-31", "time": "15:00"},
{"message": "Workouts Tips: Focus on proper nutrition before and after workouts.", "date": "2024-01-01", "time": "15:00"},
{"message": "Workouts Tips: Use foam rolling to relieve muscle tension and soreness.", "date": "2024-01-02", "time": "15:00"},
{"message": "Workouts Tips: Stay mindful of your body's limitations and avoid pushing too hard.", "date": "2024-01-03", "time": "15:00"},
{"message": "Workouts Tips: Include restorative practices like tai chi or gentle yoga for recovery.", "date": "2024-01-04", "time": "15:00"},
{"message": "Workouts Tips: Monitor your form in the mirror or with a workout partner.", "date": "2024-01-05", "time": "15:00"},
{"message": "Workouts Tips: Follow a structured workout program designed for your goals.", "date": "2024-01-06", "time": "15:00"},
{"message": "Workouts Tips: Use a timer to track your intervals and rest periods during HIIT.", "date": "2024-01-07", "time": "15:00"},
{"message": "Workouts Tips: Stay hydrated by sipping water throughout your workout.", "date": "2024-01-08", "time": "15:00"},
{"message": "Workouts Tips: Pay attention to your body's signals for when it's time to rest.", "date": "2024-01-09", "time": "15:00"},
{"message": "Workouts Tips: Experiment with different workout environments, such as home or gym.", "date": "2024-01-10", "time": "15:00"},
{"message": "Workouts Tips: Learn the principles of progressive overload for muscle growth.", "date": "2024-01-11", "time": "15:00"},
{"message": "Workouts Tips: Include cardiovascular workouts to improve heart health.", "date": "2024-01-12", "time": "15:00"},
{"message": "Workouts Tips: Focus on a balanced diet to support your fitness endeavors.", "date": "2024-01-13", "time": "15:00"},
{"message": "Workouts Tips: Use resistance training to increase bone density.", "date": "2024-01-14", "time": "15:00"},
{"message": "Workouts Tips: Prioritize proper sleep for energy and muscle recovery.", "date": "2024-01-15", "time": "15:00"},
{"message": "Workouts Tips: Avoid excessive sitting and incorporate movement throughout the day.", "date": "2024-01-16", "time": "15:00"},
{"message": "Workouts Tips: Adjust your workouts as your fitness level improves.", "date": "2024-01-17", "time": "15:00"},
{"message": "Workouts Tips: Train your mind with positive self-talk and mental strength.", "date": "2024-01-18", "time": "15:00"},
{"message": "Workouts Tips: Include meditation or mindfulness exercises for mental wellness.", "date": "2024-01-19", "time": "15:00"},
{"message": "Workouts Tips: Modify exercises if you have injuries or limitations.", "date": "2024-01-20", "time": "15:00"},
{"message": "Workouts Tips: Set a schedule for your workouts to create a routine.", "date": "2024-01-21", "time": "15:00"},
{"message": "Workouts Tips: Embrace technology, like fitness apps, for tracking progress.", "date": "2024-01-22", "time": "15:00"},
{"message": "Workouts Tips: Seek professional guidance for any persistent pain or discomfort.", "date": "2024-01-23", "time": "15:00"},
{"message": "Workouts Tips: Challenge yourself with new exercises to keep it interesting.", "date": "2024-01-24", "time": "15:00"},


]


# Sort the scheduled messages by date and time
scheduled_messages.sort(key=lambda msg: datetime.datetime.strptime(f"{msg['date']} {msg['time']}", "%Y-%m-%d %H:%M"))

# Schedule and send the messages
async def schedule_messages():
    for msg in scheduled_messages:
        delay = calculate_delay(f"{msg['date']} {msg['time']}")
        if delay > 0:
            await asyncio.sleep(delay)
        await send_scheduled_message(bot, msg["message"])

# Calculate the time delay in seconds for each message
def calculate_delay(message_time):
    now = datetime.datetime.now()
    scheduled_time = datetime.datetime.strptime(message_time, "%Y-%m-%d %H:%M")
    time_difference = scheduled_time - now
    return max(0, time_difference.total_seconds())

# Start the main loop
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(schedule_messages())
