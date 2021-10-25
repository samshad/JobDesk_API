import spacy
from collections import Counter
from check_location import is_location
import pandas as pd


nlp_wk = spacy.load('xx_ent_wiki_sm')
# doc = "The Swatch Group (Hong Kong) Limited10/F Kerry Centre683 King’s RoadQuarry BayCN-Hong Kong"
# doc = "Longines Watches Company, Francillon SA Les Longines CH-2610 Saint-Imier"


def get_loc(x):
    doc = nlp_wk(x)
    loc = []
    for ent in doc.ents:
        #print(ent, ent.label_)
        if ent.label_ == 'LOC':
            if is_location(str(ent)) is not None:
                loc.append(str(ent))
    return dict(Counter(loc))


if __name__ == '__main__':
    # doc = "job context lead design development cycle design journey mapping user flow architecture conduct usability testing develop share design vision work head marketing create design concept scratch job responsibility 3 year industry experience knowledge adobe invision photoshop illustrator indesign proficient principle framer figma effect keynote previous experience work large scale complex digital product web native background work saas ui design knowledge desire investigate innovate develop emerge design ux technology trend excellent understanding userexperience design mobile web technology trend demonstrable design skill ability relevant work ability create wireframe prototype outstande social digital fluency good communication skill employment status fulltime workplace work home work office educational requirement bachelor computer application bca experience requirements year job location dhaka salary negotiable competitive salary flexible holiday scheme friendly fun international group coworker flexible working environment blend home office publish company information azolve technologies bangladesh ltd address kawran bazar bdbl bhaban 4th floor web wwwazolvecom business azolve home gomembership wwwgomembershipcom fast grow membership event management cloud base software provider deliver solution national governing bodies sport membership lead organisation azolve build enviable global customer base lead sport organisation look scale solution worldwide azolve technologies bangladesh limited wholly subsidiary team base dhaka responsible develop deliver support gomembership software service azolve application information gomembership visit wwwgomembershipcom nbsp follow job responsibility na employment status fulltime educational requirement minimum ssc english speak skill civil engineering background knowledge concrete mix design year experience construction industry min year experience position experience requirements year additional requirement good knowledge english language computer literate immediate joining job location nigeria salary usd month compensation benefits benefit nigerian labor law publish company information urgent requirement european company nigeria follow"
    # doc = "Dhaka, Bangladesh, Education Details B.Tech Rayat and Bahra Institute of Engineering and Biotechnology Data Science Data Science Skill Details Numpy- Exprience - Less than 1 year months Machine Learning- Exprience - Less than 1 year months Tensorflow- Exprience - Less than 1 year months Scikit- Exprience - Less than 1 year months Python- Exprience - Less than 1 year months GCP- Exprience - Less than 1 year months Pandas- Exprience - Less than 1 year months Neural Network- Exprience - Less than 1 year monthsCompany Details company - Wipro description - Bhawana Aggarwal E-Mail:bhawana.chd@gmail.com Phone: 09876971076 VVersatile, high-energy professional targeting challenging assignments in Machine PROFILE SUMMARY âª An IT professional with knowledge and experience of 2 years in Wipro Technologies in Machine Learning, Deep Learning, Data Science, Python, Software Development. âª Skilled in managing end-to-end development and software products / projects from inception, requirement specs, planning, designing, implementation, configuration and documentation. âª Knowledge on Python , Machine Learning, Deep Learning, data Science, Algorithms, Neural Network, NLP, GCP. âª Knowledge on Python Libraries like Numpy, Pandas, Seaborn , Matplotlib, Cufflinks. âª Knowledge on different algorithms in Machine learning like KNN, Decision Tree, Bias variance Trade off, Support vector Machine(SVM),Logistic Regression, Neural networks. âª Have knowledge on unsupervised, Supervised and reinforcement data. âª Programming experience in relational platforms like MySQL,Oracle. âª Have knowledge on Some programming language like C++,Java. âª Experience in cloud based environment like Google Cloud. âª Working on different Operating System like Linux, Ubuntu, Windows. âª Good interpersonal and communication skills. âª Problem solving skills with the ability to think laterally, and to think with a medium term and long term perspective âª Flexibility and an open attitude to change. âª Ability to create, define and own frameworks with a strong emphasis on code reusability. TECHNICAL SKILLS Programming Languages Python, C Libraries Seaborn, Numpy, Pandas, Cufflinks, Matplotlib Algorithms KNN, Decision Tree, Linear regression, Logistic Regression, Neural Networks, K means clustering, Tensorflow, SVM Databases SQL, Oracle Operating Systems Linux, Window Development Environments NetBeans, Notebooks, Sublime Ticketing tools Service Now, Remedy Education UG Education: B.Tech (Computer Science) from Rayat and Bahra Institute of Engineering and Biotechnology passed with 78.4%in 2016. Schooling: XII in 2012 from Moti Ram Arya Sr. Secondary School(Passed with 78.4%) X in 2010 from Valley Public School (Passed with 9.4 CGPA) WORK EXPERINCE Title : Wipro Neural Intelligence Platform Team Size : 5 Brief: Wiproâs Neural Intelligence Platform harnesses the power of automation and artificial intelligence technologiesânatural language processing (NLP), cognitive, machine learning, and analytics. The platform comprises three layers: a data engagement platform that can easily access and manage multiple structured and unstructured data sources; an âintent assessment and reasoningâ engine that includes sentiment and predictive analytics; and a deep machine learning engine that can sense, act, and learn over time. The project entailed automating responses to user queries at the earliest. The Monster Bot using the power of Deep Machine Learning, NLP to handle such queries. User can see the how their queries can be answered quickly like allL1 activities can be eliminated. Entity Extractor -> This involves text extraction and NLP for fetching out important information from the text like dates, names, places, contact numbers etc. This involves Regex, Bluemix NLU apiâs and machine learning using Tensor flow for further learning of new entities. Classifier ->This involves the classifications of classes, training of dataset and predicting the output using the SKLearn classifier (MNB, SVM, SGD as Classifier) and SGD for the optimization to map the user queries with the best suited response and make the system efficient. NER: A Deep Learning NER Model is trained to extract the entities from the text. Entities like Roles, Skills, Organizations can be extracted from raw text. RNN(LSTM) Bidirectional model is trained for extracting such entities using Keras TensorFlow framework. OTHER PROJECTS Title : Diabetes Detection Brief : Developed the software which can detect whether the person is suffering from Diabetes or not and got the third prize in it. TRAINING AND CERTIFICATIONS Title: Python Training, Machine Learning, Data Science, Deep Learning Organization: Udemy, Coursera (Machine Learning, Deep Learning) Personal Profile Fatherâs Name :Mr. Tirlok Aggarwal Language Known : English & Hindi Marital Status :Single Date of Birth(Gender):1993-12-20(YYYY-MM-DD) (F) company - Wipro description - Developing programs in Python. company - Wipro description - Title : Wipro Neural Intelligence Platform Team Size : 5 Brief: Wiproâs Neural Intelligence Platform harnesses the power of automation and artificial intelligence technologiesânatural language processing (NLP), cognitive, machine learning, and analytics. The platform comprises three layers: a data engagement platform that can easily access and manage multiple structured and unstructured data sources; an âintent assessment and reasoningâ engine that includes sentiment and predictive analytics; and a deep machine learning engine that can sense, act, and learn over time. The project entailed automating responses to user queries at the earliest. The Monster Bot using the power of Deep Machine Learning, NLP to handle such queries. User can see the how their queries can be answered quickly like allL1 activities can be eliminated. Entity Extractor -> This involves text extraction and NLP for fetching out important information from the text like dates, names, places, contact numbers etc. This involves Regex, Bluemix NLU apiâs and machine learning using Tensor flow for further learning of new entities. Classifier ->This involves the classifications of classes, training of dataset and predicting the output using the SKLearn classifier (MNB, SVM, SGD as Classifier) and SGD for the optimization to map the user queries with the best suited response and make the system efficient. NER: A Deep Learning NER Model is trained to extract the entities from the text. Entities like Roles, Skills, Organizations can be extracted from raw text. RNN(LSTM) Bidirectional model is trained for extracting such entities using Keras TensorFlow framework. company - Wipro Technologies description - An IT professional with knowledge and experience of 2 years in Wipro Technologies in Machine Learning, Deep Learning, Data Science, Python, Software Development. âª Skilled in managing end-to-end development and software products / projects from inception, requirement specs, planning, designing, implementation, configuration and documentation. âª Knowledge on Python , Machine Learning, Deep Learning, data Science, Algorithms, Neural Network, NLP, GCP. âª Knowledge on Python Libraries like Numpy, Pandas, Seaborn , Matplotlib, Cufflinks. âª Knowledge on different algorithms in Machine learning like KNN, Decision Tree, Bias variance Trade off, Support vector Machine(SVM),Logistic Regression, Neural networks. âª Have knowledge on unsupervised, Supervised and reinforcement data. âª Programming experience in relational platforms like MySQL,Oracle. âª Have knowledge on Some programming language like C++,Java. âª Experience in cloud based environment like Google Cloud. âª Working on different Operating System like Linux, Ubuntu, Windows. âª Good interpersonal and communication skills. âª Problem solving skills with the ability to think laterally, dhaka, and to think with a medium term and long term perspective âª Flexibility and an open attitude to change. âª Ability to create, define and own frameworks with a strong emphasis on code reusability."
    # tf = pd.read_csv('Data/sample_test.csv')
    # doc = list(tf['text'])[0]

    # doc = "Compagnie des Montres Longines, Francillon S.A. Les Longines CH-2610 Saint-Imier"
    doc = "4452 Itingen BL"
    print(get_loc(doc))

