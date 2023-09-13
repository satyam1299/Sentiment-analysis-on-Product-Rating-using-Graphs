#!/usr/bin/env python
# coding: utf-8

# # Sentiment analysis on Product Rating using Graphs

# ## Import Libraries

# In[1]:


#importing all the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ## Converting Timestamp to date & time

# In[2]:


#from datetime import datetime

#timestamp = 1545730073
#dt_object = datetime.fromtimestamp(timestamp)

#print("dt_object =", dt_object)
#print("type(dt_object) =", type(dt_object))


# ## Admin & User data

# In[3]:


#admin data
#one list created for admin username and one dictionary created for passwords
admin_username = ['satyam12']
admin_password = {"satyam12":12111810}


#user data
#one list created for username and one dictionary created for passwords 
username = ['ayan03', 'rahul02', 'shreyash13']
password = {"ayan03":12111018, "rahul02":12110123, "shreyash13":12100120}


# ## Reading .csv file

# In[4]:


#df = pd.read_csv('C:/Users/1209s/Downloads/py_dataset/ratings_Beauty.csv')
prod_rating_data=pd.read_csv("C:/Users/1209s/Downloads/py_dataset/ratings_Beauty.csv", dtype={'Rating': 'int8'}, names=['UserId', 'ProductId','Rating','Timestamp'], index_col=None, header=0)
prod_rating_data.head() #print first 5 rows only


# ## Shape of Product Rating Dataset 

# In[5]:


prod_rating_data.shape #return total number of rows and columns of original dataset


# ## What is the number of users ,products and the total rating?

# In[6]:


print("Columns: {}".format(np.array2string(prod_rating_data.columns.values)))
print("Number of Users: {:,}".format(len(prod_rating_data.UserId.unique())))
print("Number of Products: {:,}".format(len(prod_rating_data.ProductId.unique())))
print("Number of Rating: {:,}".format(prod_rating_data.shape[0]))
print("\n")


# ## Print information about the data

# In[7]:


prod_rating_data.info() #returns data type of each column, total number of entries and memory usage
print("\n")


# In[8]:


desc = prod_rating_data.describe()['Rating'].reset_index()
print(desc,"\n")


# ## Now, lets clean our valuable data
# ## Check for Missing Values

# In[9]:


#Check for missing values
pd.DataFrame(prod_rating_data.isnull().sum().reset_index()).rename( columns={0:"Total missing","index":"Columns"})  #our data is very clean


# ## Check for Duplicate values

# In[10]:


#check for duplicate values
prod_rating_data.duplicated().sum()


# ## What is the number of ratings per product ?

# In[11]:


#sorted product Id in descending order with their Rating
product_ratings=prod_rating_data.groupby('ProductId')['Rating'].count().sort_values(ascending=False) 
print(product_ratings.head()) #returns first 5 rows
print("\n")


# ## What is the of ratings per user?

# In[12]:


#sorted User_Id in descending order
user_ratings=prod_rating_data.groupby('UserId')['Rating'].count().sort_values(ascending=False) #sorted userid with total number of ratings that they have given 
user_ratings.head() #returns first 5 rows


# ## What is the percentage of the products with 5 rate ?

# In[13]:


len(prod_rating_data[prod_rating_data.Rating==5]['ProductId'].unique())/len(prod_rating_data['ProductId'].unique()) #80% that looks good


# ## Let's describe the users :

# In[14]:


user_ratings.head()


# ## Distribution of Rating

# In[15]:


#Plot Distributin of Rating
def Rating_graph():
    #Adding dark background to the graph
    #plt.style.use("dark_background")

    #Create a distribution plot for rating
    #sns.displot(prod_rating_data.Rating, bins=20, kde = False)
    #plt.show()

    count_ratings = [0 for i in range(len(np.unique(prod_rating_data['Rating'])))]
    print("Number of Unique Ratings available : ",len(count_ratings))

    for i in range(prod_rating_data.shape[0]):
      count_ratings[int(prod_rating_data['Rating'][i]-1)]+=1

    print("Count of each ratings is : ",count_ratings)

    plt.style.use('seaborn')

    labels = ["1 star", "2 star", "3 star", "4 star", "5 star"]

    plt.figure(figsize=(15,8),facecolor="w")
    ax = plt.barh(labels,count_ratings, color=["yellow", "cyan", "pink", "skyblue", "lightgreen"], edgecolor="black")

    for i in ax.patches:
        plt.text(i.get_width()+0.6, i.get_y()+0.3, str(round((i.get_width()), 4)), fontsize=15, fontweight='bold', color='grey')

    plt.title("Distribution of Rating",fontsize=15)
    plt.show()


    #Plotting a pie chart
    percentage = np.array([183784, 113034, 169791, 307740, 1248721])
    category = ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star']
    myexplode = [0, 0, 0, 0, 0.2]
    mycolors = ['pink', 'blue', 'y', 'g', 'r']
    plt.pie(percentage, labels=category, autopct='%1.1f%%', colors=mycolors, explode=myexplode, shadow=True)
    plt.legend(title="Rating Distribution in Pie Graph", loc='lower right')
    plt.show()


# ## Number of users make different Rating

# In[16]:


high_rate=prod_rating_data[prod_rating_data.Rating==5]


# In[17]:


rate4=prod_rating_data[prod_rating_data.Rating==4]


# In[18]:


rate3=prod_rating_data[prod_rating_data.Rating==3]


# In[19]:


rate2=prod_rating_data[prod_rating_data.Rating==2]


# In[20]:


low_rate=prod_rating_data[prod_rating_data.Rating==1]


# In[21]:


#Distribution of Rating Score
def different_user_rating(): 
    """
    Below are the way to find the unique number of Rating 
    """
    print('The number of users who make 5 rate on products is :',len(high_rate['UserId'].unique()))
    print('The number of users who make 4 rate on products is :',len(rate4['UserId'].unique()))
    print('The number of users who make 3 rate on products is :',len(rate3['UserId'].unique()))
    print('The number of users who make 2 rate on products is :',len(rate2['UserId'].unique()))
    print('The number of users who make 1 rate on products is :',len(low_rate['UserId'].unique()))

    """
    Below are the way to find the total count of Rating 
    """
    #print('The number of users who make 5 rate on products is :',len(high_rate['UserId']))
    #print('The number of users who make 4 rate on products is :',len(rate4['UserId']))
    #print('The number of users who make 3 rate on products is :',len(rate3['UserId']))
    #print('The number of users who make 2 rate on products is :',len(rate2['UserId']))
    #print('The number of users who make 1 rate on products is :',len(low_rate['UserId']))


    #Plotting a pie chart
    percentage = np.array([162401, 99470, 140097, 238261, 824697])
    category = ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star']
    myexplode = [0, 0, 0, 0, 0.2]
    mycolors = ['y', 'g', 'pink', 'red', 'orange']
    plt.pie(percentage, labels=category, autopct='%1.1f%%', colors=mycolors, explode=myexplode, shadow=True)
    plt.legend(title="Rating Distribution in Pie Graph", loc='lower right')
    plt.show()


# ## Represent Product Rating in Good and Bad Category

# In[22]:


#Classify Product Rating in Good or Bad Category
#Classify rating as Good
good_rate = len(prod_rating_data[prod_rating_data['Rating'] >= 3])

#Classify rating as Bad
bad_rate = len(prod_rating_data[prod_rating_data['Rating'] < 3])

# Printing rates and their total numbers
print ('Good ratings : {} reviews for products'.format(good_rate))
print ('Bad ratings : {} reviews for products'.format(bad_rate))

#Apply the new classification to the ratings column
#prod_rating_data['rating_class'] = prod_rating_data['Rating'].apply(lambda x: 'bad' if x < 3 else'good')
#df.head()

def good_bad():
    percentage = np.array([1726252,296818])
    category = ['Good','Bad']
    myexplode = [0,0.2]
    mycolors = ['yellow','red']
    plt.pie(percentage, labels=category, autopct='%1.1f%%', colors=mycolors, explode=myexplode, shadow=True)
    plt.legend(title="Product Rating in Good or Bad Category")
    plt.show()


# ## Statistics of Numerical Values

# In[23]:


#Statistics of non-numeric variables
def stat_of_data():
    #Number of unique customers
    print('\nNumber of unique Customers : {}'.format(len(prod_rating_data['UserId'].unique())))

    #Number of unique products
    print('\nNumber of unique Products : {}'.format(len(prod_rating_data['ProductId'].unique())))

    #Rating number per unique customer
    print('\nReview per customer: {}'.format((len(prod_rating_data)/len(prod_rating_data['UserId'].unique()))))      

    #Rating number per unique product 
    print('\nReview per product: {}'.format((len(prod_rating_data)/len(prod_rating_data['ProductId'].unique()))))


# ## Top 10 Most Rated Products

# In[24]:


def top_10Products():
    Ratings = prod_rating_data.groupby(['ProductId'])['Rating'].sum().reset_index()
    Ratings.columns = ['Product ID', 'Ratings']
    y = Ratings.sort_values(by='Ratings', ascending = False).head(10).reset_index().drop('index', axis=1)
    ax = plt.axes()
    ax.set(facecolor = "black")
    sns.barplot(x=y['Product ID'],y=y['Ratings'],palette='OrRd_r',saturation=1)
    plt.xticks(rotation=90,fontsize=10)
    plt.yticks(fontsize=10)
    plt.xlabel('\nPRODUCT ID',fontsize=15)
    plt.ylabel('TOTAL RATING',fontsize=15)
    plt.title('Top 10 Most Rated Products\n',fontsize=20,fontweight="bold")
    plt.show()


# ## Top 10 Least Rated Products

# In[25]:


def bottom_10Products():
    Ratings = prod_rating_data.groupby(['ProductId'])['Rating'].sum().reset_index()
    Ratings.columns = ['Product ID', 'Ratings']
    y = Ratings.sort_values(by='Ratings', ascending = False).tail(10).reset_index().drop('index', axis=1) #ratings ordered in descending order
    ax = plt.axes()
    ax.set(facecolor = "black")
    sns.barplot(x=y['Product ID'],y=y['Ratings'],palette='gist_rainbow_r',saturation=1)
    plt.xticks(rotation=90,fontsize=10)
    plt.yticks(fontsize=10)
    plt.xlabel('\nPRODUCT ID',fontsize=15)
    plt.ylabel('TOTAL RATINGS',fontsize=15)
    plt.title('Top 10 Least Rated Products\n',fontsize=20,fontweight="bold")
    plt.show()


# In[26]:


len(prod_rating_data) - len(prod_rating_data.dropna()) #we have 0 null values


# ## Numbers of Rating each day 

# In[27]:


"""data_by_date = prod_rating_data.copy()
data_by_date.timestamp = pd.to_datetime(prod_rating_data.Timestamp, unit="s").dt.date
data_by_date = data_by_date.sort_values(by="Timestamp", ascending=False).reset_index(drop=True)
print("Number of Ratings each day:")
data_by_date.groupby("Timestamp")["Rating"].count().tail(10).reset_index()"""


# ## Number of Rating per User

# In[28]:


def product_per_user():
    rating_by_user = prod_rating_data.groupby(by='UserId')['Rating'].count().sort_values(ascending=False)

    rating_hist,  bins  = np.histogram(rating_by_user, bins=[1,2,3,4,5,10,50,100,200,400,500])
    rating_hist2, bins2 = np.histogram(rating_by_user, bins=[1,2,3,10,100000])

    figsize = (15,5)
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=figsize)

    pd.DataFrame({"Numbers of User":rating_hist,"Total Rates":bins[:-1]}).plot.bar(x="Total Rates", ax=ax1)
    ax1.set(yscale="log")
    ax1.set(ylabel="Total number of Users rated product", xlabel="Number of Products rated by a User")
    ax1.set(title="Distribution of Rating (Log Scale)")
    ax1.get_legend().remove()
    [item.set_fontsize("x-large") for item in ax1.get_yticklabels()]

    pd.DataFrame({"Numbers of User":rating_hist2,"Total Rates":bins2[:-1]}).plot.pie(x="Total Rates",y="Numbers of User", labels=[1,2,3,">10 items"], ax=ax2,legend=False, autopct='%1.1f%%', startangle=90, fontsize="x-large")
    ax2.set_ylabel('')

    plt.show()
    #Only 1.5% of users rated more than 10 products


# ## Number of Rating per Product

# In[29]:


# Review number per unique customer
#Review per customer
def rating_per_product():
    product_group = prod_rating_data.groupby('ProductId')

    #Visualizing
    Ratings = product_group.sum()['Rating']/len(prod_rating_data['ProductId'])


    #Create a distribution plot for rating
    sns.barplot(data=prod_rating_data, x='x_values', y='y_values')
    plt.show()

    #plt.figure(figsize =(20,9))
    #sns.barplot(data=prod_rating_data, x='user_unique', y='prod_rating', palette='rocket')
    #plt.show()


# ## Admin & User Operations

# In[30]:


#admin can add the user or it has also used for registration
#if I will add the user, even after successfull creation of new user. I will not be able to login to the User Portal
def add_user():
    new_user = input("Enter username: ")
    new_pass = int(input("Enter password: "))

    #insert the data in user
    #append the username in the user list
    username.append(new_user)
    #append the password in the user dictionary
    password[new_user] = new_pass
    print("\nYou have successfully created the user")
    print("\nUsers: {}".format(username))


#user can perform these operations
def user_operations():
    while(True):
        #operations available for admin
        print("\nOperations:"
              "\n1. Graphical representation of Distribution of Amazon Rating"
              "\n2. No.of people who made different rating"
              "\n3. Counts of Good and Bad Rating"
              "\n4. Statistics of Non-Numeric Data"
              "\n5. Top 10 Most Rated Products"
              "\n6. Top 10 Least Rated Products"
              "\n7. Number of Products rated by User"
              "\n8. Distribution of Average Rating"
              "\n9. Exit")
        user_choice = int(input("\nEnter your choice: "))

        match user_choice:
            case 1:
                Rating_graph()
                
            case 2:
                different_user_rating()
                
            case 3:
                good_bad() 
                
            case 4:
                stat_of_data()
                
            case 5:
                top_10Products()
                
            case 6: 
                bottom_10Products()
                
            case 7:
                product_per_user()
                
            case 8:
                pass
                
            case 9:
                break
                
            case _:
                print("\nInvalid choice!")

                
#admin can perform these operations        
def admin_operations():
    while(True):
        #operations available for admin
        print("\nOperations:"
              "\n1. View Product Rating"
              "\n2. View Users"
              "\n3. Add User"
              "\n4. Remove User (this feature is not available right now)"
              "\n5. Exit")
        admin_choice = int(input("\nEnter your choice: "))
    
    
        match admin_choice:
            case 1:
                different_user_rating() #displays data
                print("\n\n")
                Rating_graph()
                
            case 2:
                print("\nDisplay Users:")
                for i in range(0,3):
                    print(username[i])
                    
            case 3:
                print("\nAdd new user")
                add_user()
                
            case 4:
                print("This feature will be available soon")
                #code for removing particular user
                """for i in range(0,3):
                    print("{} : {}".format(i+1, username[i]))
                remove_user = input("Enter index of the user to remove: ")
                username.pop('remove_user') #you can also use remove method
                password.pop('remove_user')
                print("Users: {}".format(username))
                print("You have successfully removed the {}".format(remove_user))"""
                
            case 5:
                break
                
            case _:
                print("\nInvalid choice!")


#admin login
def admin():
    #taking input from the admin
    admin_input = input("Enter username: ")
    admin_pass = int(input("Enter password: "))
    checkpass = admin_password.get("satyam12") 
    
    if((admin_input in admin_username) and (admin_pass == checkpass)):
        print("\nWelcome {}".format(admin_input))
        admin_operations()   
    else:
        print("\nLogin Failed!")
        admin()


#user login      
def user():
    #taking input username and password from the user
    user_input = input("Enter username: ")
    pass_input = int(input("Enter password: "))
    
    #conditions to check username and password for each user
    if((user_input in username) and (pass_input == (password.get("ayan03")))):
        print("\nWelcome {}".format(user_input))
        user_operations()
    elif((user_input in username) and (pass_input == (password.get("rahul02")))):
        print("\nWelcome {}".format(user_input))
        user_operations()  
    elif((user_input in username) and (pass_input == (password.get("shreyash13")))):
        print("\nWelcome {}".format(user_input))
        user_operations()
        #elif((self.new_user in username) and (self.new_pass == (password.get(self.new_user)))):
        #print("\nWelcome {}".format(user_input))
        #user_operations()
    elif((user_input not in username) or (pass_input != (password.get("ayan03")))):
        print("\nLogin Failed!")
        user()
    elif((user_input not in username) or (pass_input != (password.get("rahul02")))):
        print("\nLogin Failed!")
        user()
    elif((user_input not in username) or (pass_input != (password.get("shreyash13")))):
        print("\nLogin Failed!")
        user()


# In[31]:


while(True):
    #creating choices for user
    print("\nWho are you?"
          "\n1. Admin Login"
          "\n2. User Login"
          "\n3. Dont have an account?"
          "\n4. Exit")
    choice = int(input("\nEnter your choice: "))

    #switch case
    match choice:
        case 1:
            print("\nAdmin Login")
            #admin login module
            #calling admin function
            admin()

        case 2:
            print("\nUser Login")
            #admin login module
            #calling user function
            user()

        case 3:
            print("\nContact admin to create an account in this system or")
            print("\nRegister to the system")
            #user can register to the system by just filling the details
            add_user()
            #after registering to the system, user can login to the system
            print("\nUser Login")
            user()

        case 4:
            break
            
        case _: #the underscore character is used as a catch-all
            print("\nInvalid choice!")


# In[ ]:




