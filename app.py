from flask import Flask, render_template, url_for, request, redirect 
# from flask_sqlalchemy import SQLAlchemy
from experta import*

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cg.db'
# db = SQLAlchemy(app)

def home ():
    return render_template("home.html")

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/public/landing')
def landing():
    return render_template('/public/index.html')

@app.route('/ptest', methods=['POST', 'GET'])
def ptest():
    return render_template('ptest.html')

class Questions(Fact):
    pass


class GetGourses(KnowledgeEngine):
    # ESTJ
    @Rule(Questions(answers=["ESTJ", "Science", "Technical", "A"]))
    def estj_STA(self):
        #self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))
        
        self.declare(Fact(courses={
        'type':'You are an ESTJ -Extrovert Sensing Thinking Judging .',
        'main':' You are organized , dedicated , honest , dignified , traditional and you belive what you do is right and socially acceptable. You often take the role of a leader and people look to you a for guidance and counsel . You are methodical , organized , dedicated , reliable and direct . You excel at the following set procedures closely and adher to guidelines . You are dedicated and hardworking . Guiding others is something you feel strongly about .  If you are an ESTJ, you may want to consider the following careers:',
        'careers':{
            'Judge':'A public official authorized to decide questions brought before a court. A judge preside over a court hearings and trials , supervise legale proceedings and uphold the rights of individuals involved in a legal process. They ensure that trials are conducted according to established rules and procedurs which may include detemining how testimony is given and evidence submitted . These professinals  can be elected by the public or appoineted by goverments. Judges often work long hours in pereparation for hearings and somtimes must trvael  for them . To be able to be a judge in kenya you must have an undergraduate degree in one of the following political science , history , business or economics  . This are offered in  - University of Nairobi. , Kenyatta University , Mount Kenya University  , Daystar University  , Strathmore University , Technical University of Kenya , JKUAT.',

            'Hotel manager':"A hotel manager is  a hospitality professional who oversees the functions of hotels , motels and resorts . They maintain operations and ensure guest satisfactoin . In many environments , a hotel manager will review their facility's budeget and revenue in order to increase profitability . Additialnally , they evalutae each department manager's performance and offer constructive feedback for imporvemnt. For you  to become a hotel manager you will need  a  diploma or a bachelor's degree in hospitality this is offered in Karatina University , Kericho Teachers Training College , The Kisumu Natialnal Polytechnic , Tangasa University College-Nairobi, Egerton University Njoro Campus, Moi Univerisity Kitale Campus , Daystar Univeristy - Nairobi , Garissa University , Maasai Mara University , Kabarak University , KCA University , Kenyatta University School of Hospitality and Tourism ",

            "Chief Executive Officer":"There is no better role for an ESTJ than the title of CEO. The chief executive officer , also somtimes called the managing director, is the company leader . The CEO is in charge of all business operations and ventures . They report only to the board of directors . Ulitmate responsibility for the success of the enterpricse rests with  the CEO , making ESTJs an excellent fit to handle this presssure and reward. To become a CEO you will need a minimum of 5 years or more of related work experience and education level in business administration . School offering  business adminstration are Eastern and Southern Africa Management Institute - Nairobi, Institute of Advanced Technology IAT Nairobi , Kenya Institute of Applied Sciences - Eldoret, Institute of Advanced Techonology  School of Businnes - Nairobi , Egerton University , Kenya Airways Limited Pride Center- Nairobi, The Kisumu National Polytechnic - Kisumu, Nyeri National Polytechnic- Nyeri , East Africa School of Management - Nairobi ",
            "Coach":"",
            "Financial officer":"",
            "Real estate agent":"",
            
            },
        'careersToAvoid':{
            "Actors":"Actors do not enjoy the consistency that ESTJs prefer . Artistic careers such as acting can involve erratic work schedules and varied work environments , and those  are things that do not appeal to ESTJ personality types. Actors also need to be able to follow direction from others and acting doesn't provide opportunities to give direction or offer traditional goal-setting opportunities . No formal training is necessary to be an actor , although taking studies in theater is common .",
            
            "Taxi Drivers and Chauffeurs":" Taxi drivers and chauffers are transportation specialist who take people from location to location . They may need to ear a specific license to operate their vehicle , but do not need postsecondary training and typically learn on the job . ESTJ personaly types may apperciate the opportunites to interact with their clients , but will find that this career field offers no opportunities to set goals and that they do not work in a structued environment."
        }
        }))

    @Rule(Questions(answers=["ESTJ", "Science", "Technical", "B"]))
    def estj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge','Military', "Police",'Civil Servant', "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ESTJ", "Science", "Technical", "C"]))
    def estj_STC(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge','Military', 'Police', 'Civil Service', 'Technical teaching']))
        
    @Rule(Questions(answers=["ESTJ", "Science", "Technical", "D"]))
    def estj_STD(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge','Police','Civil Service', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["ESTJ", "Science", "Corporate", "A"]),Questions(answers=["ESTJ", "Science", "Corporate", "B"]),Questions(answers=["ESTJ", "Science", "Corporate", "C"]),Questions(answers=["ESTJ", "Science", "Corporate", "D"])))
    def estj_SC(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ESTJ", "Art", "Technical", "A"]),Questions(answers=["ESTJ", "Art", "Technical", "B"])))
    def estj_ATAB(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge', "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Technical", "C"]))
    def estj_ATC(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Technical", "D"]))
    def estj_ATD(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Technical Teacher"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Corporate", "A"]))
    def estj_ACA(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Corporate", "B"]))
    def estj_ACB(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Corporate", "C"]))
    def estj_ACC(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge',"Financial Officer"]))

    @Rule(Questions(answers=["ESTJ", "Art", "Corporate", "D"]))
    def estj_ACD(self):
        self.declare(Fact(courses=['You are an ESTJ - They are known as natural leaders who work best while in charge', 'civil service']))

    #ENTP
    @Rule(Questions(answers=["ENTP", "Science", "Technical", "A"]))
    def entp_STA(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity','Entrepreneur', 'Psychologist', 'Consultant','Engineer', 'Computer Programmer', 'Psychiatrist']))

    @Rule(Questions(answers=["ENTP", "Science", "Technical", "B"]))
    def entp_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity','Entrepreneur', 'Psychologists', 'Consultant', 'Scientist', 'Programmer']))

    @Rule(Questions(answers=["ENTP", "Science", "Technical", "C"]))
    def entp_STC(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity','Consultant','Entrepreneur']))
        
    @Rule(Questions(answers=["ENTP", "Science", "Technical", "D"]))
    def entp_STD(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity','Entrepreneur']))

    @Rule(OR(Questions(answers=["ENTP", "Science", "Corporate", "A"]),Questions(answers=["ENTP", "Science", "Corporate", "B"]),Questions(answers=["ENTP", "Science", "Corporate", "C"]),Questions(answers=["ENTP", "Science", "Corporate", "D"])))
    def entp_SC(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Enterpreneur"]))

    @Rule(OR(Questions(answers=["ENTP", "Art", "Technical", "A"]),Questions(answers=["ENTP", "Art", "Technical", "B"]), Questions(answers=["ENTP", "Art", "Technical", "c"])))
    def entp_ATAB(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Entrepreneur", "Photographer", "Consultant", "Sales Representative", 'Marketer', 'Public relations', 'Journalism']))

    @Rule(Questions(answers=["ENTP", "Art", "Technical", "D"]))
    def entp_ATD(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Entrepreneur", 'Actor']))

    @Rule(Questions(answers=["ENTP", "Art", "Corporate", "A"]))
    def entp_ACA(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Consultant"]))

    @Rule(Questions(answers=["ENTP", "Art", "Corporate", "B"]))
    def entp_ACB(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Consultant"]))

    @Rule(Questions(answers=["ENTP", "Art", "Corporate", "C"]))
    def entp_ACC(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity',"Consultant"]))

    @Rule(Questions(answers=["ENTP", "Art", "Corporate", "D"]))
    def entp_ACD(self):
        self.declare(Fact(courses=['You are an ENTP- You are freedom oriented and need a career that allows you to act independently while expressing your creativity', 'Consultant']))

    #ENTJ
    @Rule(OR (Questions(answers=["ENTJ", "Science", "Technical", "A"]), (Questions(answers=["ENTJ", "Science", "Technical", "B"]))))
    def entj_STA(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding','Organisation Founder', "Entrepreneur", "Computer Consultant", "Professor", "Department Manager"]))

    @Rule(Questions (answers=["ENTJ", "Science", "Corporate", "C"]))
    def entj_STB(self):
    #    print("Engineering")
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding','Administrator', "Entrepreneur"]))
    
    @Rule(Questions (answers=["ENTJ", "Science", "Corporate", "D"]))
    def entj_SCD(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding', "Entrepreneur"]))


    @Rule(Questions(answers=["ENTJ", "Science", "Technical", "C"]))
    def entj_STC(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding','Organisation founder', 'Politician', 'Department Manager']))
        
    @Rule(Questions(answers=["ENTJ", "Science", "Technical", "D"]))
    def entj_STD(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding','Organisation founder', 'Entrepreneur']))

    @Rule(OR(Questions(answers=["ENTJ", "Science", "Corporate", "A"]),Questions(answers=["ENTJ", "Science", "Corporate", "B"])))
    def entj_SC(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ENTJ", "Art", "Technical", "A"]),Questions(answers=["ENTJ", "Art", "Technical", "B"])))
    def entj_ATAB(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Entreprneur", "Judge", "Lawyer", "Professor", 'Politician', 'Department Manager']))

    @Rule(OR(Questions(answers=["ENTJ", "Art", "Technical", "C"]), Questions(answers=["ENTJ", "Art", "Technical", "D"])))
    def entj_ATC(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Entrepreneur", "Manual Laborer", 'Politician']))

   # @Rule
   # def entj_ATD(self):
   #     self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Technical Teacher"]))

    @Rule(OR(Questions(answers=["ENTJ", "Art", "Corporate", "A"]), (Questions(answers=["ENTJ", "Art", "Corporate", "B"])) ))
    def entj_ACA(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"CEO", "Business Analyst", "Business Administrator", 'Manager', 'Entrepreneur']))

 #   @Rule(Questions(answers=["ENTJ", "Art", "Corporate", "B"]))
  #  def entj_ACB(self):
   #     self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ENTJ", "Art", "Corporate", "C"]))
    def entj_ACC(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding',"Business Administrator", 'Business Manager' ]))

    @Rule(Questions(answers=["ENTJ", "Art", "Corporate", "D"]))
    def entj_ACD(self):
        self.declare(Fact(courses=['You are an ENTJ- You are a natural born leader who steers towards a vision using your understanding', 'Entrepreneur']))

    #ENFP
    @Rule( OR (Questions(answers=["ENFP", "Science", "Technical", "A"]), (Questions(answers=["ENFP", "Science", "Technical", "B"]))))
    def enfp_STA(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity','Organisation founder', "Entrepreneur", "Computer Consultant", "Professor", "Department manager"]))

    
   # def enfp_STB(self):
    #    print("Engineering")
     #   self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ENFP", "Science", "Technical", "C"]))
    def enfp_STC(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity','Organisation founder', 'Politician', 'Department Manager']))
        
    @Rule(Questions(answers=["ENFP", "Science", "Technical", "D"]))
    def enfp_STD(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity','Organisation founder', 'Entrepreneur']))

    @Rule(OR(Questions(answers=["ENFP", "Science", "Corporate", "A"]),Questions(answers=["ENFP", "Science", "Corporate", "B"]),))
    def enfp_SC(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"CEO",'Business Executive', 'Enrepreneur']))

    @Rule(Questions(answers=["ENFP", "Science", "Corporate", "C"]))
    def enfp_SCC(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Administrator", 'Enrepeneur']))
    
    @Rule(Questions(answers=["ENFP", "Science", "Corporate", "D"]))
    def enfp_SCD(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Entrepreneur"]))

    @Rule(OR(Questions(answers=["ENFP", "Art", "Technical", "A"]),Questions(answers=["ENFP", "Art", "Technical", "B"])))
    def enfp_ATAB(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Entrepreneur", "Judge", "Lawyer", "Professor", 'Politician', 'Manual Laborer', 'Department Manager']))

    @Rule( OR (Questions(answers=["ENFP", "Art", "Technical", "C"]), (Questions(answers=["ENFP", "Art", "Technical", "D"]))))
    def enfp_ATC(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Politician", "Entrepreneur", 'Manual laborer',]))

   # @Rule
   # def enfp_ATD(self):
   #     self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Technical Teacher"]))

    @Rule(OR(Questions(answers=["ENFP", "Art", "Corporate", "A"]), (Questions(answers=["ENFP", "Art", "Corporate", "B"])) ))
    def enfp_ACA(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"CEO", "Business Analyst", "Business administrator", 'Manager', 'Entrepreneur']))

   # @Rule
   # def enfp_ACB(self):
   #     self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ENFP", "Art", "Corporate", "C"]))
    def enfp_ACC(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity',"Business administrator", 'Business Manager']))

    @Rule(Questions(answers=["ENFP", "Art", "Corporate", "D"]))
    def enfp_ACD(self):
        self.declare(Fact(courses=['You are an ENFP- Creative, fun loving and excel at careers that allow you to  express your ideas and spontanity', 'Entrepreneur']))

    #ENFJ
    @Rule(Questions(answers=["ENFJ", "Science", "Technical", "A"]))
    def enfj_STA(self):
        self.declare(Fact(courses={
        'type':'You are an ENFJ - Extrovert Intuition Feeling Judging .',

        "main":"Those classified as ENFJ have a strong presence and natural leadership skills. They can be honest about their ideas and opinions while being mindful of others' feelings. The ENFJ will also commonly articulate and defend her believes.These individuals are extremely driven, but they don't let this distract them from the needs of those around them. They are typically empathetic and will intuitively find ways to help those around them. They feel compelled to make the world a better place and constantly look for opportunities to improve things.Characteristics that describe most ENFJ individuals are : Charismatic , Confident , Empathic , Energetic , Passionate",
        'careers':{
            
            "Guidance counselor":"ENFJs' highly empathic nature makes them very good at counseling others. They're naturally inclined to try to learn more about the people around them and find ways to help. As a guidance counselor, this type of person can satisfy their desire to help others improve their lives every day. Some of the best ENFJ jobs are those that are directly related to creating a positive experience for other people.",
            
            "Teacher":"One of the common nicknames for the ENFJ personality type is 'the teacher,' so it's no surprise that this career is well-suited to these individuals. They are skilled at explaining concepts to others based on their learning style. ENFJs are also highly empathetic, which is an important skill for teachers who need to evaluate and understand their students' thoughts and feelings. A teacher with an ENFJ personality is likely good at relating to her students and finding meaningful ways to connect with them.",
            
            "Public relations account manager":"Understanding the needs and motivations of others is also invaluable in a public relations career. ENFJs often find that they intuitively know how to navigate difficult or sensitive situations. They're also very self-controlled and self-directed, which helps them excel in this fast-paced field. The creative nature of the ENFJ individual is also valuable in public relations as these professionals must know how to appeal to the public effectively for brands and organizations.",
            
            "Sales manager":"Personal interaction is important to ENFJs, which makes them competitive candidates for sales manager roles. These individuals enjoy the process of finding out what others are interested in and identifying ways to meet people's needs. Well-organized and self-motivated, an ENFJ doesn't need much outside motivation to build a large client list. This personality type is perfect for a salesperson who works with products or services she personally believes in.",

            "Art director":"ENFJs often have a strong interest in the arts. They are also good at evaluating and understanding the preferences of others. These skills all transfer well to art director positions. In this field, an ENFJ would likely be very good at identifying concepts that would appeal to a large number of people. Their natural teaching and communication skills are also valuable for pitching ideas to clients.",

            "Human resources director":"Charming and sociable, ENFJs are easy for others to relate to. This makes them well-suited to a job in human relations where they're tasked with making the workplace comfortable and productive for employees. An ENFJ's intuition also helps them understand others' emotions well, which makes them excellent communicators."
             
            },
        'careersToAvoid':{
            
            "Accountant":"ENFJ individuals typically require a decent amount of personal interaction. Accountants and other financial specialists typically spend more time working alone. ",
            
            "IT specialist":"An ENFJ should probably avoid work in IT and other areas that focus more on technology and equipment than on people.",
            
            "Law enforcement":"While there are many aspects of law enforcement that may appeal to an ENFJ, this can be a difficult path for these individuals to pursue. Negative outcomes weigh heavily on those with this type of personality.",

            "Mechanical engineer":"Working closely with machinery is might be too impersonal of a career for most ENFJ personality types. The work in this field also tends to be clear-cut when ENFJs enjoy working with nuance and ambiguity.",

            "Researcher":"While ENFJs enjoy learning, they do it better in a social environment where they interact closely with others and explore topics in a hands-on way."

            
        }
        }))

    @Rule(Questions(answers=["ENFJ", "Science", "Technical", "B"]))
    def enfj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ENFJ", "Science", "Technical", "C"]))
    def enfj_STC(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["ENFJ", "Science", "Technical", "D"]))
    def enfj_STD(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["ENFJ", "Science", "Corporate", "A"]),Questions(answers=["ENFJ", "Science", "Corporate", "B"]),Questions(answers=["ENFJ", "Science", "Corporate", "C"]),Questions(answers=["ENFJ", "Science", "Corporate", "D"])))
    def enfj_SC(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ENFJ", "Art", "Technical", "A"]),Questions(answers=["ENFJ", "Art", "Technical", "B"])))
    def enfj_ATAB(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Technical", "C"]))
    def enfj_ATC(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Technical", "D"]))
    def enfj_ATD(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Technical Teacher"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Corporate", "A"]))
    def enfj_ACA(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Corporate", "B"]))
    def enfj_ACB(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Corporate", "C"]))
    def enfj_ACC(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills',"Financial Officer"]))

    @Rule(Questions(answers=["ENFJ", "Art", "Corporate", "D"]))
    def enfj_ACD(self):
        self.declare(Fact(courses=['You are an ENFJ- You encourage others to actualize themselves and show excelent leadership and interpersonal skills']))

    #ESTP
    @Rule(OR(Questions(answers=["ESTP", "Science", "Technical", "A"]), Questions(answers=["ESTP", "Science", "Technical", "B"]), Questions(answers=["ESTP", "Science", "Technical", "C"])))
    def estp_STA(self):
        self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people','Military', "Police", "Paramedic", "Medical Technician",' Entrepreneur', "Computer technician",'Fire Fighter']))

 #   @Rule()
 #   def estp_STB(self):
 #       print("Engineering")
 #       self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people','Military', "Police", "Nurse", "Technical Teacher"]))

  #  @Rule)
   # def estp_STC(self):
    #    self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["ESTP", "Science", "Technical", "D"]))
    def estp_STD(self):
        self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people','Police', 'Entrepreneur']))

    @Rule(OR(Questions(answers=["ESTP", "Science", "Corporate", "A"]),Questions(answers=["ESTP", "Science", "Corporate", "B"]),Questions(answers=["ESTP", "Science", "Corporate", "C"]),Questions(answers=["ESTP", "Science", "Corporate", "D"])))
    def estp_SC(self):
        self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ESTP", "Art", "Technical", "A"]),Questions(answers=["ESTP", "Art", "Technical", "B"]), Questions(answers=["ESTP", "Art", "Technical", "C"]), Questions(answers=["ESTP", "Art", "Technical", "D"])))
    def estp_ATAB(self):
        self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people', 'Farmer', "Craftsman", "Transport Coordinator", "Carpenter", "Entrepreneur"]))

    @Rule(OR(Questions(answers=["ESTP", "Art", "Corporate", "A"]),Questions(answers=["ESTP", "Art", "Corporate", "B"]), Questions(answers=["ESTP", "Art", "Corporate", "C"]), Questions(answers=["ESTP", "Art", "Corporate", "D"])))
    def estp_ACA(self):
        self.declare(Fact(courses=['You are an ESTP- You have a gift for reacting and solving problems as well as persuading people', "Social Worker", "Entrepreneur "]))

    #ESFP
    @Rule(OR(Questions(answers=["ESFP", "Science", "Technical", "A"]), Questions(answers=["ESFP", "Science", "Technical", "B"])))
    def esfp_STA(self):
        #self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational','Teacher', "Counsillor", "Social Worker", "Child care", "Consultant", 'Therapist']))
        self.declare(Fact(courses={
        'type':'You are an ESFP - Extrovert Sensing Feeling Perceiving .',
        "main":"ESFPs typically enjoy the spotlight. Bubbly and engaging.  ESFPs are excellent at entertaining, but they're not self-centered. Rather, they have strong emotional intelligence and excel at reading the moods of those around them. An ESFP can easily adjust her presentation to suit her audience.An ESFP is naturally entertaining to be around and seek out the beauty in everything they find, whether they're marveling at nature on a hike or swooning over apparel on the runway. Some terms that naturally describe an ESFP individual are:     Spontaneous  ,  Fun-loving  ,  Warm  ,  Personable  ,  Playful  ,  Open  ,  Active  ,  Energetic ",

        'careers':{
            
            "Sales representative":"Sales representatives are responsible for attending to the needs for a client or book of clients. Common tasks include following up with clients and leads , creating ROI and sales presentations and finding the right products and services to fit a client's needs. ESFPs are great at building and maintaining relationships , which is key to any sales representative's success.",

            "Event planner":"The best ESFP careers are those that give these individuals the chance to earn money with activities they would already be doing. An ESFP will likely spend plenty of her free time planning gatherings. As an event planner, he can turn this trait into a lucrative job. Event planners can specialize in specific events such as corporate gatherings, trade shows, press events or weddings.",

            "Cosmetologist":"Whether they're applying makeup or styling hair, ESFPs can apply their personable nature and attention to detail in this field. Though an ESFP knows how to command attention, these individuals are also very attentive to the needs of others, which makes them especially skilled at coming up with the right look for any client.",

            "Professional entertainer":"ESFPs with a talent for acting, singing, comedy or any other type of performance art are likely to succeed in show business. These same talents can be put to work in more traditional careers as well, such as motivational speaking, corporate training or education.",

            "Flight attendant":"Flight attendants must be flexible, easygoing and attentive. These requirements are rarely a challenge for an ESFP. These individuals are often looking to expand their social circles and meet new people and are usually comfortable working with all types of people. This personality type is well equipped for the task of welcoming passengers onto the plane and keeping them comfortable throughout their flight. An ESFP may also enjoy taking advantage of the opportunity to travel, experience new places and take on a new group of people each time the plane takes flight.",

            "Vacation planner":"ESFPs have a knack for creativity and originality while keeping practicality in mind. As vacation planners, these individuals will be able to combine inventive ideas with workable arrangements to put together great travel experiences for their clients. Their observant natures will also help them pinpoint the types of vacations that are best for each customer.",

            "Tour guide":"As a tour guide, an ESFP gets to interact with others every day. They're resourceful and flexible, which will help them deal with the varying needs of different groups. As strong speakers, ESFPs typically have no trouble giving presentations to travelers. These individuals are usually good at working with people and enjoy socializing with a diverse group of personalities around them. The best ESFP personality careers in this area are those with a variety of tasks as well, such as a position that includes many different tours."
            
            },
        'careersToAvoid':{
            
            "Technial writer":"Though ESFPs are creative, they do a better job of displaying this trait in front of a crowd than on a piece of paper. Writing is a solitary career that won't give an ESFP the amount of social interaction that he needs.",

            "Accountant":"Accounting is a satisfying career for those who enjoy logic and order, but ESFPs are more flexible and creative. They crave interaction with people more than numbers. ",

            "Human resources":"HR professionals have a lot of contact with people, which may draw an ESFP in. However, the shine will quickly wear off of this type of job as it becomes routine. "

            
        }
        }))

    @Rule(Questions(answers=["ESFP", "Science", "Technical", "C"]))
    def esfp_STC(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational','Teacher', "Counsillor", "Social Worker", "Child care", "Consultant"]))
        
    @Rule(Questions(answers=["ESFP", "Science", "Technical", "D"]))
    def esfp_STD(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational','Police', 'Child care giver']))

    @Rule(OR(Questions(answers=["ESFP", "Science", "Corporate", "A"]),Questions(answers=["ESFP", "Science", "Corporate", "B"]),Questions(answers=["ESFP", "Science", "Corporate", "C"]),Questions(answers=["ESFP", "Science", "Corporate", "D"])))
    def esfp_SC(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational',"Consultant"]))

    @Rule(OR(Questions(answers=["ESFP", "Art", "Technical", "A"]),Questions(answers=["ESFP", "Art", "Technical", "B"]),Questions(answers=["ESFP", "Art", "Technical", "C"])))
    def esfp_ATAB(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational',"Actor", "Painter", "Comedian", "Sales", 'Teaching', 'Fashion Design', 'Interior Design','Photography','Music','Human Resource','Cleric','Coach']))

    @Rule(Questions(answers=["ESFP", "Art", "Technical", "D"]))
    def esfp_ATD(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational',"Actor",'Painter','Comedian','Photgrapher','Musician','Cleric','Coach']))

    @Rule(Questions(answers=["ESFP", "Art", "Corporate", "A"]))
    def esfp_ACA(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational']))

    @Rule(Questions(answers=["ESFP", "Art", "Corporate", "B"]))
    def esfp_ACB(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational']))

    @Rule(Questions(answers=["ESFP", "Art", "Corporate", "C"]))
    def esfp_ACC(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational']))

    @Rule(Questions(answers=["ESFP", "Art", "Corporate", "D"]))
    def esfp_ACD(self):
        self.declare(Fact(courses=['You are an ESFP- You are Optimistic, Fun-Loving and your enthusiasm is motivational']))

    #ESFJ
    @Rule(Questions(answers=["ESFJ", "Science", "Technical", "A"]))
    def esfj_STA(self):
        #self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))
        self.declare(Fact(courses={
        'type':'You are an ESFJ - Extrovert Sensing Feeling Judging .',

        "main":"ESFJs are serious and practical, committed to their responsibilities , and sensitive to the needs of others. They strive for harmony and are generous with their time , efforts , and emotions , and are eager to please --both at home and at work. ESFJs value loyalty and tradition and hold to a strict moral code. They typically enjoy their routines and maintain a regular schedule that allows them to stay organized and productive. Because ESFJs are sympathetic to the needs of others , they're quick to lend a helping hand. Due to their strong sense of order and a desire for solidarity , they often assume professional roles that allow them to establish and maintain structures and processes. Because ESFJs seek cooperation and harmony in the workplace , they gravitate toward roles that allow them to enforce social order. Often, there is no gray area with this personality type: to them, actions are either right or wrong, and their orderliness and practicality prompt them to expect the same from others. As long as they maintain a consistent routine, ESFJs can be comfortable in a variety of career fields. Sensitive to the feelings of others , this personality is skilled at social interaction and adept at reading social cues. Driven by a strong sense of duty, they are loyal to their workplace and usually quite popular. ",

        'careers':{
            
            "Photojournalist":"",
            
            "Technical support specialist":"",
            
            "Corporate ins":"",
            
            "Editor":"",
            
            "Librarian":"",
            
            "College professor":"",
            
            "Medical researcher":"",
             
            },
        'careersToAvoid':{

            "Software developer":"",
            
            "Freelancer":"",
            
            "Actor":"",
            
            "Attorney":"",
            
            "Journalist":""
            
        }
        }))

    @Rule(Questions(answers=["ESFJ", "Science", "Technical", "B"]))
    def esfj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ESFJ", "Science", "Technical", "C"]))
    def esfj_STC(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["ESFJ", "Science", "Technical", "D"]))
    def esfj_STD(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["ESFJ", "Science", "Corporate", "A"]),Questions(answers=["ESFJ", "Science", "Corporate", "B"]),Questions(answers=["ESFJ", "Science", "Corporate", "C"]),Questions(answers=["ESFJ", "Science", "Corporate", "D"])))
    def esfj_SC(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ESFJ", "Art", "Technical", "A"]),Questions(answers=["ESFJ", "Art", "Technical", "B"])))
    def esfj_ATAB(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Technical", "C"]))
    def esfj_ATC(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Technical", "D"]))
    def esfj_ATD(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Technical Teacher"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Corporate", "A"]))
    def esfj_ACA(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Corporate", "B"]))
    def esfj_ACB(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Corporate", "C"]))
    def esfj_ACC(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships',"Financial Officer"]))

    @Rule(Questions(answers=["ESFJ", "Art", "Corporate", "D"]))
    def esfj_ACD(self):
        self.declare(Fact(courses=['You are an ESFJ- You apply natural warmth at building relationships']))

    #INTP
    @Rule(Questions(answers=["INTP", "Science", "Technical", "A"]))
    def intp_STA(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["INTP", "Science", "Technical", "B"]))
    def intp_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["INTP", "Science", "Technical", "C"]))
    def intp_STC(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["INTP", "Science", "Technical", "D"]))
    def intp_STD(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["INTP", "Science", "Corporate", "A"]),Questions(answers=["INTP", "Science", "Corporate", "B"]),Questions(answers=["INTP", "Science", "Corporate", "C"]),Questions(answers=["INTP", "Science", "Corporate", "D"])))
    def intp_SC(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Civil Servant"]))

    @Rule(OR(Questions(answers=["INTP", "Art", "Technical", "A"]),Questions(answers=["INTP", "Art", "Technical", "B"])))
    def intp_ATAB(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INTP", "Art", "Technical", "C"]))
    def intp_ATC(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INTP", "Art", "Technical", "D"]))
    def intp_ATD(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Technical Teacher"]))

    @Rule(Questions(answers=["INTP", "Art", "Corporate", "A"]))
    def intp_ACA(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["INTP", "Art", "Corporate", "B"]))
    def intp_ACB(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["INTP", "Art", "Corporate", "C"]))
    def intp_ACC(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination',"Financial Officer"]))

    @Rule(Questions(answers=["INTP", "Art", "Corporate", "D"]))
    def intp_ACD(self):
        self.declare(Fact(courses=['You are an INTP- Highly Nalytical and can easily discover patterns. You work best when allowed to use your Imagination']))

    #INFJ
    @Rule(OR(Questions(answers=["INFJ", "Science", "Technical", "A"]), Questions(answers=["INFJ", "Science", "Technical", "B"])))
    def infj_STA(self):
        self.declare(Fact(courses={
        "type":"You are an INFJ - Introvert Intution Feeling Judging .",

        "main":" This personality type is known for being insightful, creative and decisive, all of which are qualities that make them an excellent fit for certain career paths. Learn more about the unique skills and abilities associated with INFJ types, and find out which jobs are the best fit for people with this personality. Their intuitive nature allows them to interpret and add meaning when presented with information. They make choices based on feeling, which involves taking emotions and complex circumstances into account. They tend to be decisive and trust their judgment when evaluating a situation or person. The following characteristics are considered to be the most common INFJ personality traits:    Altruistic    Creative    Decisive    Dedicated    Empathetic    Helpful    Idealist    Insightful    Loyal    Quiet    Reflective    Strategic .  When it comes to their careers, INFJ types like to work independently or in small groups. They appreciate a peaceful work environment that provides time to fully develop their ideas. They are deep thinkers who like to apply their intellect to work challenges. Once INFJ types develop a plan, they are good at following through. They are empathetic and caring individuals, so most people with this personality type pursue a meaningful career that contributes to the well-being of others. ",

        'careers':{
            "Human resources professional":"A human resources (HR) manager is responsible for recruiting, interviewing and hiring new staff as well as serving as the link between the company's employees and management. This role is responsible for developing and implementing plans and procedures, like personnel policies and overseeing the work of the HR department. An HR manager has several responsibilities related to coordinating the administrative functions of an organization, including: Conducting new employee orientations and exit interviews, Writing job descriptions and placing job ads, Analyzing and updating the company's salary budget , Recommending new personnel policies and procedures as needed , Developing HR department goals and objectives. Education While some companies may allow experience as a substitute for a degree, HR manager positions typically require a bachelor's degree, ideally in human resources, finance, information technology, education, business management or a related field. Higher-level positions such as a senior HR manager may require a Master's Degree in Human Resources or Business Administration (MBA). ",

            "Entrepreneur":"",

            "Environmental officer":"",
            
            "Office manager":"An office manager uses organizational and management skills to facilitate and support the operation of a business office . They complete the necessary administrative tasks to keep the office running efficiently . Office managers also have the following responsibilities: Maintaining office procedures including payroll , scheduling and processing of paperwork, Organizing record-keeping systems including filing , protecting , accessing and destroying employee documents. , Creating and managing office budgets and bookkeeping activities. , Hiring training and supervising other administrative employees. , Planning and coordination employee meetings and work-related events. Education - A minimum of a high school diploma or equivalent is required to be an office manager. Many employers , would choose someone with a bachelors's degree . Related degress include business administration , human resources management or information management.", 

            "Product manager":"",

            "Project coordinator/manager":"",

            "Research associate":"",
            
            "Training specialist":""
                    
             
            },
        'careersToAvoid':{
            
            "Accounting and finance": "Jobs that focus more on profit and the bottom line than human elements can be frustrating for INFJ types.",

            "Emergency medical technician": "The unpredictable and sometimes chaotic nature of this job can be overwhelming for an INFJ type who loves order and quiet.",

            "Engineer": "This job involves too much practical, technical work as opposed to the intellectual, inquisitive thought that INFJ types like best.",

            "Military officer": "For INFJ types, it's very difficult to follow rigid instructions without concern for personal situations and emotions.",

            "Restaurant manager": "Restaurant workplaces tend to feel too noisy and unorganized for introverted types.",

            "Sales representative": "While INFJs may make great salespeople, the typical extroversion of these professionals and the nature of the work may be unenjoyable and uncomfortable for INFJs.",

            "Politician": "INFJs likely won't tolerate some of the necessary navigation it takes to be successful in politics. They may, however, find adjacent work interesting to help underserved or underrepresented members of the community, such as positions that help change or maintain policies."

        }
        }))

    @Rule(Questions(answers=["INFJ", "Science", "Technical", "C"]))
    def infj_STC(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality','Concillor', 'Teacher', 'Mechanic','Child Worker', 'Educational Consultant','Scientist','Social Worker']))
        
    @Rule(Questions(answers=["INFJ", "Science", "Technical", "D"]))
    def infj_STD(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality','Child Worker', 'Social Worker']))

    @Rule(OR(Questions(answers=["INFJ", "Science", "Corporate", "A"]),Questions(answers=["INFJ", "Science", "Corporate", "B"]),Questions(answers=["INFJ", "Science", "Corporate", "C"]),Questions(answers=["INFJ", "Science", "Corporate", "D"])))
    def infj_SC(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality',]))

    @Rule(OR(Questions(answers=["INFJ", "Art", "Technical", "A"]),Questions(answers=["INFJ", "Art", "Technical", "B"]), Questions(answers=["INFJ", "Art", "Technical", "C"])))
    def infj_ATAB(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality',"Clergy ", "Missionary", "Writer", "Writer", 'Music', 'Art','Photo','Librarian']))

    @Rule(Questions(answers=["INFJ", "Art", "Technical", "D"]))
    def infj_ATD(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality',"Clergy", 'Missionary', 'Music',]))

    @Rule( OR(Questions(answers=["INFJ", "Art", "Corporate", "A"]), Questions(answers=["INFJ", "Art", "Corporate", "B"]), Questions(answers=["INFJ", "Art", "Corporate", "C"]), Questions(answers=["INFJ", "Art", "Corporate", "D"]) ))
    def infj_ACA(self):
        self.declare(Fact(courses=['You are an INFJ- You are blessed with an idealistic vision and work best when trying to make a vision reality']))


    #INTJ
    @Rule(Questions(answers=["INTJ", "Science", "Technical", "A"]))
    def intj_STA(self):
        #self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))
        self.declare(Fact(courses={
        'type':'You are an INTJ - Introvert Intuition Thinking Judging .',

        "main":"The INTJ type is guided by reason and logic and has a thirst for knowledge. They are highly confident and seek to reform and improve the world around them. Even though they have lots of self-confidence, INTJs can be uncomfortable in large groups or among people they don't know well. They prefer to bond over ideas rather than engage in superficial small talk.Their talent for recognizing deeper connections and possibilities makes INTJs natural problem solvers who seek to improve themselves and the world around them. Because they are highly analytical, INTJs may struggle to understand people who rely more on emotions than reason in their decision making. Due to their independent nature, INTJs are selective in their relationships and prefer the company of like-minded thinkers. However, their thirst for knowledge drives them to learn from others and engage in collaborative conversation. INTJs can also have judgemental and perfectionist tendencies-this can be an asset when they are tasked with producing high quality work but it can also cause tension in some workplace relationships.",

        'careers':{
            "Finacial advisor":"",
            "Accountant":"",
            "Auditor":"",
            "Economist":"",
            "School administrator":"",
            "Guidance counselor":"",
            "Paralegal":"",
            "Personal trainer":"",
            "Physician":"",
             
            },
        'careersToAvoid':{
            "Real estate agent":"",
            "Chilcare worker ":"",
            "Police officer":"",
            
        }
        }))

    @Rule(Questions(answers=["INTJ", "Science", "Technical", "B"]))
    def intj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["INTJ", "Science", "Technical", "C"]))
    def intj_STC(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["INTJ", "Science", "Technical", "D"]))
    def intj_STD(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["INTJ", "Science", "Corporate", "A"]),Questions(answers=["INTJ", "Science", "Corporate", "B"]),Questions(answers=["INTJ", "Science", "Corporate", "C"]),Questions(answers=["INTJ", "Science", "Corporate", "D"])))
    def intj_SC(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Civil Servant"]))

    @Rule(OR(Questions(answers=["INTJ", "Art", "Technical", "A"]),Questions(answers=["INTJ", "Art", "Technical", "B"])))
    def intj_ATAB(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INTJ", "Art", "Technical", "C"]))
    def intj_ATC(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INTJ", "Art", "Technical", "D"]))
    def intj_ATD(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Technical Teacher"]))

    @Rule(Questions(answers=["INTJ", "Art", "Corporate", "A"]))
    def intj_ACA(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["INTJ", "Art", "Corporate", "B"]))
    def intj_ACB(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["INTJ", "Art", "Corporate", "C"]))
    def intj_ACC(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies',"Financial Officer"]))

    @Rule(Questions(answers=["INTJ", "Art", "Corporate", "D"]))
    def intj_ACD(self):
        self.declare(Fact(courses=['You are an INTJ- You are good at grasping difficult complex concepts and building strategies']))

    #INFP
    @Rule(Questions(answers=["INFP", "Science", "Technical", "A"]))
    def infp_STA(self):
        # self.declare(Fact(courses=['You are an INFP- You ahve a strong sense of personal values, are highly creative and offer support from behind the scenes','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))

        self.declare(Fact(courses={
        'type':'You are an INFP - Introvert Intuition Feeling Perceving .',
        'main':'  INFPs are quiet and prefer not to talk about themselves. They enjoy spending time alone in quiet places. They love analyzing signs and symbols and enjoy getting lost in their imagination and daydreams. In professional environments, INFPs seek to learn new things and change the world. While they usually bring intensity and enthusiasm to projects, they often find it challenging to sustain their excitement for long periods of time. If you are an INFP, some careers you may want to consider are:',
        
        'careers':{
        
            "Writer":"INFP Personality Types have great skills for expression, both verbal and written, making a career as a writer an ideal choice. Whether authoring a novel, writing a blog, or drafting long-form investigative pieces for a newspaper, INFPs would especially excel in this career if given the opportunity to write about a topic that was meaningful to them. To become a writer, a bachelor's degree in journalism, communications, or English is typically a good starting point. ",

            "Social Worker":"Social workers work with individuals, families, and communities during times of hardship, such as providing help to a single mother, or working with a community that is poverty-stricken. They work closely with individuals and may develop close relationships, connecting individuals with various state, federal, and private assistance programs. An INFP Personality Type would do well as a social worker because this field allows them to bring positive change to the lives of many people through communication and problem solving skills. Entry-level social workers generally need a bachelor's degree in social work, though some individuals may also wish to pursue a master's degree to have other opportunities in this field. ",

            "School and Career Counselor":"School and career counselors work with students as they make decisions regarding their studies and future careers. An INFP Personality Type would relish the opportunity to provide personalized guidance and career planning for students. These professionals assist with students' academic and personal issues, and provide tools for goal setting. To become a school and career counselor, you will need to achieve a master's degree in counseling and be licensed by the state in which you work.",

            "Physical Therapist":"An INFP Personality Type would make an excellent physical therapist because their unrelenting sense of optimism would likely help clients and patients who are undergoing painful physical therapy. Physical therapists diagnose ailments and create personalized therapy plans for recovery and wellness. Many physical therapists develop personal relationships with their clients, which an INFP greatly enjoys. Physical therapists must complete a Doctor of Physical Therapy program in order to practice. ",
        
            "Editor":"",
        
            "Graphic Designer":"",
        
            "Photographer":"",
        
            "Film editor":"",
        
            "Videographer":"",
        
            "Interpreter or translator":"",
        
            "Editorial director":"",
        
            "Technical writer":"",
        
            "Content strategist":"",
        
            "Human resources manager":"",
        
            "Fundraising manager":"",
        
            "UX designer":"",
        
            "Design technologist":"",




            },
        'careersToAvoid':{
        
            "Retail Sales Workers":"Retail sales workers, who only need on-the-job training, may help customers locate items, take payments for purchases, and arrange products in the store. INFP personalities may find that this type of work offers limited opportunities to use their creativity and that it lacks the meaning they desire from their work. Retail sales workers typically have a pretty consistent work routine as well, and the lack of variety may not appeal to INFP personality types. ",
            
            "Principals":"School principals have a lot of people and resources that they oversee. They normally need a master's degree and license, and they use their skills to make decisions about things like school schedules and budgets. Those with an INFP personality may find it overwhelming to deal with so many people on a regular basis; INFPs are introverts and tend to prefer working with people one-on-one or in small groups, and addressing an entire school population or groups of parents may not appeal to them. Principals also have to make a lot of conventional decisions, which is not one of the INFP strengths." ,
            
            "Sales Manager":"",
            
            "Performer":"",
            
            "Police Officer":"",
        }
        }))

    @Rule(Questions(answers=["INFP", "Science", "Technical", "B"]))
    def infp_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an INFP- You ahve a strong sense of personal values, are highly creative and offer support from behind the scenes','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["INFP", "Science", "Technical", "C"]))
    def infp_STC(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["INFP", "Science", "Technical", "D"]))
    def infp_STD(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["INFP", "Science", "Corporate", "A"]),Questions(answers=["INFP", "Science", "Corporate", "B"]),Questions(answers=["INFP", "Science", "Corporate", "C"]),Questions(answers=["INFP", "Science", "Corporate", "D"])))
    def infp_SC(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Civil Servant"]))

    @Rule(OR(Questions(answers=["INFP", "Art", "Technical", "A"]),Questions(answers=["INFP", "Art", "Technical", "B"])))
    def infp_ATAB(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INFP", "Art", "Technical", "C"]))
    def infp_ATC(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["INFP", "Art", "Technical", "D"]))
    def infp_ATD(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Technical Teacher"]))

    @Rule(Questions(answers=["INFP", "Art", "Corporate", "A"]))
    def infp_ACA(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["INFP", "Art", "Corporate", "B"]))
    def infp_ACB(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["INFP", "Art", "Corporate", "C"]))
    def infp_ACC(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes',"Financial Officer"]))

    @Rule(Questions(answers=["INFP", "Art", "Corporate", "D"]))
    def infp_ACD(self):
        self.declare(Fact(courses=['You are an INFP- You have a strong sense of personal values, are highly creative and offer support from behind the scenes']))

    #ISTP
    @Rule(OR(Questions(answers=["ISTP", "Science", "Technical", "A"]), Questions(answers=["ISTP", "Science", "Technical", "B"])))
    def istp_STA(self):
        #self.declare(Fact(courses=['You are an ISTP- You stay calm under pressure, excel at jobs needing immediate attention','Military', "Police", "Detectives ", "Forensics", "Programmer", 'Computer and System analyst', 'Engineer', 'Mechanic','Pilot','Driver','Entrepreneur','Fire-Fighter','Paramedic','Dentist',]))
        self.declare(Fact(courses={
        'type':'You are an ISTP - Introvert Sensing Thinking Perceiving .',
        
        "main":"People with this personality type focus on information and facts when making decisions. ISTP types are also very adaptable and perceptive.In their work, ISTP personality types are known for their ability to troubleshoot problems in a practical manner. They prefer to do most of their work independently and can maintain a clear focus on the task at hand. ISTP types are generally quiet and observant, but they collaborate well with others when needed.Many ISTP personality types pursue a career in which they can produce tangible results. Many prefer analytical or technical tasks that allow them to apply practical solutions without bias or emotional considerations, which they find distracting in a work setting. When problems come up, they can adjust and find a quick solution. This personality type values efficiency and logic in their work and is known to go the extra mile to see a project through to the end. The following personality traits are closely associated with ISTP types: Capable, Curious, Detail oriented , Efficient , Flexible , Logical , Observant , Practical , Problem-solver ",
        
        'careers':{
            
            "Engineer":"Any kind of engineering work is a great fit for someone with an ISTP personality type. Their analytical minds are capable of grasping the intricate inner workings of things. As a computer hardware engineer, for example, an ISTP type can enjoy troubleshooting issues and putting together efficient computer systems.Engineering tasks also utilize this personality type's critical thinking skills and preference for logical solutions. ISTP personality types like the fact that engineering produces tangible results that have a practical purpose in the real world. The independent nature of this work is also appealing to ISTP types.",

            "Technician": "Like engineering, technician work requires knowing the ins and outs of complex machinery. ISTP personality types are well-suited to this type of work since they enjoy troubleshooting problems. Whether they are working on airplanes, HVAC equipment or electrical systems, ISTP types get to put their problem-solving and logic skills to good use in this career path.People with this personality type excel at installing, maintaining and repairing a wide variety of equipment. Many technicians work individually or in small teams, which appeals to the introverted nature of ISTP types.",

            "Construction worker": "Construction work gives ISTP personality types the opportunity to get involved in hands-on projects with a practical purpose. Those who like to be active with their work enjoy the physical element of constructing and renovating buildings. It also offers the opportunity to find logical solutions for building challenges. ISTP types have a detail-oriented nature that helps them make sure each task is done correctly and efficiently",

            "Inspector":"Jobs like building inspector or health inspector are appealing to ISTP types since this work requires an analytical, detail-oriented mind. This personality type is adept at memorizing and applying a wide variety of rules and regulations. ISTP types don't like to rush through tasks, so they will take the time needed to be thorough in every inspection. The independent nature of the work appeals to quiet ISTP types.",

            "Machinist": "Working with expensive and potentially dangerous equipment requires intense focus and attention to detail. Because ISTP personality types excel in both of these areas, they are well-suited to working as a machinist. This is also a great job for ISTP types because workers get to see the fruits of their labor being produced in real-time. Machinist work is solitary, which allows people with this personality to enjoy the kind of quiet, intense work they prefer.",

            "Forensic Scientist": "Forensic science requires excellent attention to detail, problem-solving skills and critical thinking skills. For these reasons, it's a great fit for ISTP types. It involves tangible evidence, such as fingerprints and DNA, and much of the work takes place in a quiet lab environment. From collecting and analyzing samples to writing reports and recalling details during court testimony, the job requirements of a forensic scientist make good use of the traits associated with the ISTP personality type. "
             
            },
        'careersToAvoid':{
            
            "Artist":"Although ISTP types like to create tangible things in their work, they prefer practical work to creative pursuits.",

            "Clergy":"As with social work, this career path is not a good fit for the ISTP type's preference for logical, analytical tasks.",

            "Manager":" ISTP types prefer to work on detailed tasks rather than deal with coworker dynamics and big-picture projects.",

            "Marketer":"There are no clear-cut solutions to marketing challenges, which can be frustrating for problem-solving ISTP types."

            
        }
        }))

    @Rule(Questions(answers=["ISTP", "Science", "Technical", "C"]))
    def istp_STC(self):
        self.declare(Fact(courses=['You are an ISTP- You stay calm under pressure, excel at jobs needing immediate attention','Military', 'Police', "Detectives ", "Forensics", "Programmer", 'Computer and System analyst','Mechanic','Driver','Entrepreneur']))
        
    @Rule(Questions(answers=["ISTP", "Science", "Technical", "D"]))
    def istp_STD(self):
        self.declare(Fact(courses=['You are an ISTP- You stay calm under pressure, excel at jobs needing immediate attention','Police', 'Mechanic', 'Driver', 'Entreprneur']))

    @Rule(OR(Questions(answers=["ISTP", "Science", "Technical", "A"]),Questions(answers=["ISTP", "Science", "Technical", "B"]),Questions(answers=["ISTP", "Science", "Technical", "C"]),Questions(answers=["ISTP", "Science", "Technical", "D"])))
    def istp_SC(self):
        self.declare(Fact(courses=['You are an ISTP- You stay calm under pressure, excel at jobs needing immediate attention',"Carpenter",'Athlete','Entrepreneur', 'Construction worker', 'Farmer', 'Steel Worker']))

    @Rule(OR(Questions(answers=["ISTP", "Science", "Corporate", "A"]),Questions(answers=["ISTP", "Science", "Corporate", "B"]),Questions(answers=["ISTP", "Science", "Corporate", "C"]),Questions(answers=["ISTP", "Science", "Corporate", "D"])))
    def istp_ACA(self):
        self.declare(Fact(courses=['You are an ISTP- You stay calm under pressure, excel at jobs needing immediate attention','Entepreneur']))

    #ISTJ
    @Rule(Questions(answers=["ISTJ", "Science", "Technical", "A"]))
    def istj_STA(self):
        #self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))
        #courses={'main':'You are an ISTJ - You are a person who appers serious and formal. You love  traditions and believe in values like honor, hard work and social responsibility. You are typically reserved, quiet, calm and upright. At work, you are known for being responsible and reliable. You thrive in an organized workplace and prefer to have rules laid out for you.  You like to use analytical and critical thought and you are highly detail-oriented. If you are an ISTJ, you may want to consider the following roles:', 'roles':['Dentist','Supply chain manager', 'Business analyst']}
        #self.declare(Fact(courses=['You are an ISTJ - You are a person who appers serious and formal. You love  traditions and believe in values like honor, hard work and social responsibility.',' You are typically reserved, quiet, calm and upright.','  At work, you are known for being responsible and reliable.',' You thrive in an organized workplace and prefer to have rules laid out for you. ',' You like to use analytical and critical thought and you are highly detail-oriented.',' If you are an ISTJ, you may want to consider the following roles:']))
        #self.declare(Fact(courses))
        self.declare(Fact(courses={
        "type":"You are an ISTJ - Introvert Sensing Thinking Judging .",

        "main":"People with this personality generally appear serious and formal. They usually love traditions and believe in values like honor, hard work and social responsibility. They are typically reserved, quiet, calm and upright. At work, they are known for being responsible and reliable. They thrive in an organized workplace and prefer to have rules laid out for them. They like to use analytical and critical thought and are highly detail-oriented. If you are an ISTJ, you may want to consider the following roles:",

        "careers":{
            "Business analyst":"ISTJ types love order and structure, which makes them a good fit for a business analyst position. This job involves gathering, organizing and processing data to come up with decisive recommendations about the business. Working with concrete numbers and statistics is something that ISTJ types excel at and enjoy. Managing and sorting through lots of information is easy for ISTJ types since they are very organized and detail-oriented. This is offered in SCHOOL OF BUSINESS in .  - University of Nairobi. , Kenyatta University , Mount Kenya University  , Daystar University  , Strathmore University , Technical University of Kenya , JKUAT.",
            
            "Supply chain manager":"As supply chain managers, ISTJ personality types get to use their skills to figure out the complicated logistics of a company's supply chain. Their detail-oriented approach ensures that all data is tracked efficiently, while their critical-thinking skills help them to come up with solutions for distribution challenges. Supply chain management involves a lot of moving parts, and ISTJ types relish the chance to make sure everything functions smoothly and efficiently to maximize profits. Offered in University of Nairobi , Kenyatta university , Machakos University College, Daystar University , KCA University  , JKUAT , Kenyatta University ",

            "Certified public accountant":"Working as a CPA is a great way for ISTJ types to demonstrate their analytical abilities. This career offers the chance to work with concrete data and make sure everything adheres to strict regulations. ISTJ types are responsible rule followers as well, which makes them trustworthy when it comes to managing money and investments. Much of the work is done independently and takes place in a quiet, structured environment. This career is stable and predictable, which people with this personality type commonly appreciate. This is offered in KCA Technical College",

            "Dentist":"ISTJ types excel in dentistry due to the detail-oriented and orderly nature of the work. Dentists practice in quiet, clean offices and usually work independently. The tasks of the job, including patient exams, analyzing x-rays and diagnosing dental issues, are fairly predictable and make good use of this personality type's logical thought processes. ISTJ types are skilled at maintaining focus on complex dental tasks, like filling cavities, extracting teeth and applying sealants or crowns. Colleges and Universities offering Bachelor of Denatal Surgery in Kenya : Moi University , University of Nairobi, Mt. Kenya University Nakuru Campus, Kenyatta University",

            "Bank Teller":"Because ISTJ types are methodical and detail-oriented, a job as a bank teller is a great fit for their skills. This position requires a high level of responsibility which trustworthy ISTJ types are adept at handling. They are also good at noting discrepancies and following strict rules, which helps them to prevent fraud and ensure that all financial transactions are completed accurately. This personality type excels at following detailed guidelines for processing deposits, withdrawals, transfers, money orders and other types of transactions. This is offered in KCA Technical College, University of nairobi , Kenyatta university , Daystar University , JKUAT , Moi University  in School of Business ",
             
            },
        "careersToAvoid":{
            "Bartender":"This type of job is very social, which can be exhausting for introverted ISTJ types.",
            "Event Management":"Frequent last-minute changes and difficult dynamics with certain clients would be frustrating for an ISTJ type.",
            "Public relations":"ISTJ types prefer a job that keeps them out of the public eye.",
        }
        }))

    @Rule(Questions(answers=["ISTJ", "Science", "Technical", "B"]))
    def istj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ISTJ", "Science", "Technical", "C"]))
    def istj_STC(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["ISTJ", "Science", "Technical", "D"]))
    def istj_STD(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["ISTJ", "Science", "Corporate", "A"]),Questions(answers=["ISTJ", "Science", "Corporate", "B"]),Questions(answers=["ISTJ", "Science", "Corporate", "C"]),Questions(answers=["ISTJ", "Science", "Corporate", "D"])))
    def istj_SC(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ISTJ", "Art", "Technical", "A"]),Questions(answers=["ISTJ", "Art", "Technical", "B"])))
    def istj_ATAB(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Technical", "C"]))
    def istj_ATC(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Technical", "D"]))
    def istj_ATD(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Technical Teacher"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Corporate", "A"]))
    def istj_ACA(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Corporate", "B"]))
    def istj_ACB(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Corporate", "C"]))
    def istj_ACC(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes',"Financial Officer"]))

    @Rule(Questions(answers=["ISTJ", "Art", "Corporate", "D"]))
    def istj_ACD(self):
        self.declare(Fact(courses=['You are an ISTJ- You have a knack for memorization and work well behind the scenes']))

    #ISFP
    @Rule( OR (Questions(answers=["ISFP", "Science", "Technical", "A"]), Questions(answers=["ISFP", "Science", "Technical", "B"])))
    def isfp_STA(self):
        #self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others','Child care', "Social work", "Teacher", "Vetenary officer", "Forest Rangers", 'Dentists', 'Medics', 'Nurse','Mechanic','Physio-Therapists']))
        self.declare(Fact(courses={
        'type':'You are an ISFP - Introvert Sensing Feeling Perceiving .',
        "main":"This personality type is strongly associated with creativity, energy and spontaneity. ISFP types are friendly and approachable, but some of their best work is done independently. Their ability to think creatively allows them to be excellent problem-solvers and innovators in the workplace.ISFP types learn quickly and approach their work with passion. Many choose careers that allow them to have a positive impact on others. A desk job in an office may feel tedious or stifling to ISFP personality types as they typically prefer hands-on work in an energetic environment. Despite their preference for a non-traditional workspace, ISFP personality types work well with deadlines and are capable of staying organized when managing multiple projects. They tend to work better on short-term projects as opposed to long-term planning. The following traits are closely associated with the ISFP personality type:    Adventurous    Artistic,  Competitive, Considerate,  Cooperative,   Creative,    Curious,    Energetic,    Flexible,    Independent,    Non-confrontational,    Quiet,    Sensitive",
        'careers':{
            "Occupational therapist":"ISFP personality types enjoy helping others and applying creative problem-solving skills. These two abilities are the core of occupational therapy. In this role, ISFP types can come up with individualized rehabilitation plans to help their patients build or restore important skills. This type of work requires adaptability, passion and creativity, all of which are areas in which ISFP personality types excel.",

            "Marketer":"ISFP personality types are known to be sensitive and perceptive, which helps them to understand others. These traits are useful in marketing, where catering to a specific audience is the key to success. As a marketing manager, ISFP personality types are capable of managing multiple projects and meeting strict deadlines. At the same time, this career provides an opportunity to be creative through various marketing campaigns. This personality type is especially gifted when it comes to brainstorming to come up with unique ideas.",

            "Chef":"Careers in the restaurant industry are a great match for the energy, creativity and spontaneity of the ISFP personality type. There are several opportunities for experimentation when working in a kitchen. Chefs can work as part of a team while still enjoying independence in how they create their own dishes. The fast-paced environment is fulfilling for someone with this kind of personality. Also, ISFP types enjoy the ability to easily move from job to job and potentially work anywhere in the world using their culinary skills.",

            "Artist":"Creative thinkers like ISFP personality types are well-suited to artistic careers. Jobs like photographer, sculptor or musician are great for ISFP types who are gifted when it comes to the arts. While it can be difficult to earn a steady income with some artistic pursuits, other jobs in this field can be quite lucrative, such as art director, interior designer or graphic designer. Artistic jobs tend to include hands-on work that ISFP types enjoy. Those who prefer to work solo might like freelance work that involves a wide variety of short-term projects through their work with various clients.",

            "Teacher":"ISFP personality types like to share their passion with others. This quality makes them excellent teachers in a wide range of fields. ISFP types who enjoy working with kids might want to teach at the elementary level. Those who enjoy exploring academic topics could make excellent university professors. Some translate their artistic skills into a teaching career (dance instructor, music teacher) in which they can help to nurture these skills in others. The ability to develop creative lesson plans and hands-on activities is a great fit for ISFP skills and interests.",

            "Environmental Scientist":"ISFP personality types have curious minds and problem-solving capabilities that make them a good fit for some scientific careers. Environmental science is an especially good fit as it involves a combination of time in the field and in the lab, which matches up well with an ISFP type's preference for hands-on, independent work. Working on critical environmental issues also gives this personality type the satisfaction of a career which can contribute positively to the lives of others."

            
             
            },
        'careersToAvoid':{
            "Accountant":"This type of work feels monotonous and boring to most ISFP types.",

            "Attorney":"The rigidity of the law tends to be unappealing to creative ISFP types.",
            
            "Manager":" ISFP types prefer to work alone rather than focus on coordinating teams",
            
            "Psychologist":"ISFP types struggle with the long-term planning involved in counseling others.",
            
            "Salesperson":"This job requires an intense level of socializing that ISFP types do not enjoy.",
            
            "Surgeon":"Long hours spent in an operating room can grueling for spontaneous ISFP types.",
        }
        }))

    @Rule(Questions(answers=["ISFP", "Science", "Technical", "C"]))
    def isfp_STC(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others','Child care', 'Social work', 'Counsillor','Teacher','Veternary officer','Forest rangers','Mechanic','Physio-Therapist']))
        
    @Rule(Questions(answers=["ISFP", "Science", "Technical", "D"]))
    def isfp_STD(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others','Child care', 'Mechanic']))

    @Rule(OR(Questions(answers=["ISFP", "Science", "Corporate", "A"]),Questions(answers=["ISFP", "Science", "Corporate", "B"]),Questions(answers=["ISFP", "Science", "Corporate", "C"]),Questions(answers=["ISFP", "Science", "Corporate", "D"])))
    def isfp_SC(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others']))

    @Rule(OR(Questions(answers=["ISFP", "Art", "Technical", "A"]),Questions(answers=["ISFP", "Art", "Technical", "B"]),Questions(answers=["ISFP", "Art", "Technical", "C"])))
    def isfp_ATAB(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others',"Music", "Composer", "Designer", "Book Keeper",'Carpenter','Cleric','Secretary','Waiter']))

    @Rule(Questions(answers=["ISFP", "Art", "Technical", "D"]))
    def isfp_ATD(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others',"Music", "Composer", "Designer", "Book Keeper",'Carpenter','Cleric','Secretary','Waiter']))

    @Rule(OR(Questions(answers=["ISFP", "Art", "Corporate", "A"]),Questions(answers=["ISFP", "Art", "Corporate", "B"]),Questions(answers=["ISFP", "Art", "Corporate", "C"])))
    def isfp_ACA(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others', "Secretary", "Book Keeper "]))

    @Rule(Questions(answers=["ISFP", "Art", "Corporate", "D"]))
    def isfp_ACD(self):
        self.declare(Fact(courses=['You are an ISFP- You tend to do well in the arts, help others and work well with others','Book Keeper']))

    #ISFJ
    @Rule(Questions(answers=["ISFJ", "Science", "Technical", "A"]))
    def isfj_STA(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed','Military', "Police", "Civil Servant", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ISFJ", "Science", "Technical", "B"]))
    def isfj_STB(self):
        print("Engineering")
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed','Military', "Police", "Nurse", "Technical Teacher"]))

    @Rule(Questions(answers=["ISFJ", "Science", "Technical", "C"]))
    def isfj_STC(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed','Military', 'Police', 'Nurse']))
        
    @Rule(Questions(answers=["ISFJ", "Science", "Technical", "D"]))
    def isfj_STD(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed','Police', 'Technical Teacher']))

    @Rule(OR(Questions(answers=["ISFJ", "Science", "Corporate", "A"]),Questions(answers=["ISFJ", "Science", "Corporate", "B"]),Questions(answers=["ISFJ", "Science", "Corporate", "C"]),Questions(answers=["ISFJ", "Science", "Corporate", "D"])))
    def isfj_SC(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Civil Servant"]))

    @Rule(OR(Questions(answers=["ISFJ", "Art", "Technical", "A"]),Questions(answers=["ISFJ", "Art", "Technical", "B"])))
    def isfj_ATAB(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Business Administrator", "Manager", "Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Technical", "C"]))
    def isfj_ATC(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Technical Teacher", "Insurance Agent"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Technical", "D"]))
    def isfj_ATD(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Technical Teacher"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Corporate", "A"]))
    def isfj_ACA(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Judge", "Financial Officer", "Insurance Agent"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Corporate", "B"]))
    def isfj_ACB(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Financial Officer", "Underwriter"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Corporate", "C"]))
    def isfj_ACC(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed',"Financial Officer"]))

    @Rule(Questions(answers=["ISFJ", "Art", "Corporate", "D"]))
    def isfj_ACD(self):
        self.declare(Fact(courses=['You are an ISFJ- You are tradition oriented, down to earth, helpful and fit in where a structure is needed']))

# -------------------------------------------------------------------------------------------------------#
class PersonalityTest(KnowledgeEngine):
    # def __init__(self):
    #     self.course = ""
    @Rule(Questions(answers=["Extrovert", "Intuition", "Thinking","Perceiving"]))
    def entp(self):
        self.declare(Fact(personality=['ENTP']))

    @Rule(Questions(answers=["Extrovert", "Intuition", "Thinking","Judging"]))
    def entj(self):
        self.declare(Fact(personality=['ENTJ']))

    @Rule(Questions(answers=["Extrovert", "Intuition", "Feeling","Perceiving"]))
    def enfp(self):
        self.declare(Fact(personality=['ENFP']))

    @Rule(Questions(answers=["Extrovert", "Intuition", "Feeling","Judging"]))
    def enfj(self):
        self.declare(Fact(personality=['ENFJ']))

    @Rule(Questions(answers=["Extrovert", "Sensing", "Thinking","Perceiving"]))
    def estp(self):
        self.declare(Fact(personality=['ESTP']))

    @Rule(Questions(answers=["Extrovert", "Sensing", "Thinking","Judging"]))
    def estj(self):
        self.declare(Fact(personality=['ESTJ']))
    
    @Rule(Questions(answers=["Extrovert", "Sensing", "Feeling","Perceiving"]))
    def esfp(self):
        self.declare(Fact(personality=['ESFP']))

    @Rule(Questions(answers=["Extrovert", "Sensing", "Feeling","Judgning"]))
    def esfj(self):
        self.declare(Fact(personality=['ESFJ']))

    @Rule(Questions(answers=["Introvert", "Intuition", "Thinking","Perceiving"]))
    def intp(self):
        self.declare(Fact(personality=['INTP']))

    @Rule(Questions(answers=["Introvert", "Intuition", "Thinking","Judging"]))
    def intj(self):
        self.declare(Fact(personality=['INTJ']))

    @Rule(Questions(answers=["Introvert", "Intuition", "Feeling","Perceiving"]))
    def infp(self):
        self.declare(Fact(personality=['INFP']))
    
    @Rule(Questions(answers=["Introvert", "Intuition", "Feeling","Judging"]))
    def infj(self):
        self.declare(Fact(personality=['INFJ']))

    @Rule(Questions(answers=["Introvert", "Sensing", "Thinking","Perceiving"]))
    def istp(self):
        #self.declare(Fact(personality=['ISTP']))
        self.declare(Fact(courses={
        'type':'You are an ISTP - Introvert Sensing Thinking Perceiving .',
        "main":"People with this personality type focus on information and facts when making decisions. ISTP types are also very adaptable and perceptive.In their work, ISTP personality types are known for their ability to troubleshoot problems in a practical manner. They prefer to do most of their work independently and can maintain a clear focus on the task at hand. ISTP types are generally quiet and observant, but they collaborate well with others when needed.Many ISTP personality types pursue a career in which they can produce tangible results. Many prefer analytical or technical tasks that allow them to apply practical solutions without bias or emotional considerations, which they find distracting in a work setting. When problems come up, they are able to adjust and find a quick solution. This personality type values efficiency and logic in their work and is known to go the extra mile in order to see a project through to the end. The following personality traits are closely associated with ISTP types: Capable , Curious,  Detail oriented ,     Efficient,     Flexible,     Logical,    Observant,    Practical,    Problem-solver,    Quiet,    Rational,    Reflective. People who are categorized as the ISTP personality type usually enjoy thought-provoking work with a hands-on element. They are well-suited for careers that require the use of their practical skills and technical interests. Here are a few of the best ISTP career matches to consider if you have this personality type.",
        'careers':{
            "Engineer":"Any kind of engineering work is a great fit for someone with an ISTP personality type. Their analytical minds are capable of grasping the intricate inner workings of things. As a computer hardware engineer, for example, an ISTP type can enjoy troubleshooting issues and putting together efficient computer systems. Engineering tasks also utilize this personality type's critical thinking skills and preference for logical solutions. ISTP personality types like the fact that engineering produces tangible results that have a practical purpose in the real world. The independent nature of this work is also appealing to ISTP types.",

            "Technician":"Like engineering, technician work requires knowing the ins and outs of complex machinery. ISTP personality types are well-suited to this type of work since they enjoy troubleshooting problems. Whether they are working on airplanes, HVAC equipment or electrical systems, ISTP types get to put their problem-solving and logic skills to good use in this career path. People with this personality type excel at installing, maintaining and repairing a wide variety of equipment. Many technicians work individually or in small teams, which appeals to the introverted nature of ISTP types.",

            "Construction worker":"Construction work gives ISTP personality types the opportunity to get involved in hands-on projects with a practical purpose. Those who like to be active with their work enjoy the physical element of constructing and renovating buildings. It also offers the opportunity to find logical solutions for building challenges. ISTP types have a detail-oriented nature that helps them make sure each task is done correctly and efficiently.",
            
            "Inspector":"Jobs like building inspector or health inspector are appealing to ISTP types since this work requires an analytical, detail-oriented mind. This personality type is adept at memorizing and applying a wide variety of rules and regulations. ISTP types don't like to rush through tasks, so they will take the time needed to be thorough in every inspection. The independent nature of the work appeals to quiet ISTP types.",
            
            "Machinist":"Working with expensive and potentially dangerous equipment requires intense focus and attention to detail. Because ISTP personality types excel in both of these areas, they are well-suited to working as a machinist. This is also a great job for ISTP types because workers get to see the fruits of their labor being produced in real time. Machinist work is solitary, which allows people with this personality to enjoy the kind of quiet, intense work they prefer.",
            
            "Forensic scientist":"Forensic science requires excellent attention to detail, problem-solving skills and critical thinking skills. For these reasons, it's a great fit for ISTP types. It involves tangible evidence, such as fingerprints and DNA, and much of the work takes place in a quiet lab environment. From collecting and analyzing samples to writing reports and recalling details during court testimony, the job requirements of a forensic scientist make good use of the traits associated with the ISTP personality type. ",
             
            },
        'careersToAvoid':{
            "Artist":"Although ISTP types like to create tangible things in their work, they prefer practical work to creative pursuits.", 
            
            "Clergy": "As with social work, this career path is not a good fit for the ISTP type's preference for logical, analytical tasks.",

            "Manager": "ISTP types prefer to work on detailed tasks rather than deal with coworker dynamics and big-picture projects.",

            "Marketer": "There are no clear-cut solutions to marketing challenges, which can be frustrating for problem-solving ISTP types.",

            "Receptionist": "The social requirements of this job are usually overwhelming for an introverted ISTP type.",

            "Social worker": "Working with vulnerable populations can be emotionally taxing, especially for ISTP types."
        }
        }))

    @Rule(Questions(answers=["Introvert", "Sensing", "Thinking","Judging"]))
    def istj(self):
        self.declare(Fact(personality=['ISTJ']))

    @Rule(Questions(answers=["Introvert", "Sensing", "Feeling","Perceiving"]))
    def isfp(self):
        self.declare(Fact(personality=['ISFP']))

    @Rule(Questions(answers=["Introvert", "Sensing", "Feeling","Judging"]))
    def isfj(self):
        self.declare(Fact(personality=['ISFJ']))


@app.route('/api/getCourses', methods=['POST'])
def getCourses():
    req_data = request.get_json()
    engine = GetGourses()
    engine.reset()
    engine.declare(Questions(answers=req_data['answers']))
    engine.run()
    # print(engine.facts)
    import json
    return(json.dumps({"courses": engine.facts[2]['courses']}, separators=(',', ':')))


@app.route('/suggestion', methods=['POST'])
def getPersonality():
    # req_data = request.form()
    print(request.form["question1"],request.form["question2"],request.form["question3"],request.form["question4"])
    engine = PersonalityTest()
    engine.reset()
    engine.declare(Questions(answers=[request.form["question1"],request.form["question2"],request.form["question3"],request.form["question4"]]))
    engine.run()
    # print(engine.facts[2]['personality'][0])
    engine1 = GetGourses()
    engine1.reset()
    engine1.declare(Questions(answers=[engine.facts[2]['personality'][0],request.form["question5"],request.form["question6"],request.form["question7"]]))
    engine1.run()
    print(engine1.facts)
    import json
    # return(json.dumps({"courses": engine1.facts[2]['courses']}, separators=(',', ':')))
    return render_template('suggestion.html', courses=engine1.facts[2]['courses'])

if __name__ == "__main__":
    app.run(debug=True)
