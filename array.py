#What is an Array?
#Array হল একটি data structure যা একই ধরনের data একসাথে সংরক্ষণ করে। এটি একটি ordered collection যা indexed হয়, অর্থাৎ প্রতিটি element এর একটি নির্দিষ্ট অবস্থান থাকে। Array সাধারণত fixed size হয়, যার মানে আপনি array তৈরি করার সময় তার আকার নির্ধারণ করতে হবে এবং পরে তা পরিবর্তন করা যাবে না।
#Array মানে খুব সহজভাবে বললে — এক ধরনের data structure যেখানে একই ধরনের অনেকগুলো data একসাথে রাখা হয়।
array = [1,2,3,4,5]

print("array:", array)

#accessing array elements
print("first element:", array[0])
print("second element:", array[1])
print("third element:", array[2])

#modifying array elements
array[0] = 10
print("modified array:", array)

#array length
print("array length:", len(array))


#array slicing
print("array slice [1:4]:", array[1:4])
print("array slice [:3]:", array[:3])   
print("array slice [2:]:", array[2:])

