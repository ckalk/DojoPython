''' Assignment: Dictionary in, tuples out -- Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")] '''

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_to_list_of_tuples(obj):
    list_tuples = []
    for key,value in obj.iteritems():
        new_tuple = (key, value)
        # print new_tuple
        list_tuples.append(new_tuple)
    return list_tuples
        
print "list of tuples:", dict_to_list_of_tuples(my_dict)