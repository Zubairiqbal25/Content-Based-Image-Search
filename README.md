<h1>INTRODUCTION</h1><br/>
     <p> In this project we are working on Content-Based Image Retrieval. Content base search is one of the hot topic now a days. As time is passed data of image get increase with the passage of time with increasing of dataset as it easily data available for research there are also many challenge are come to face for training our model. If dataset set get increase images we also need to train our model in more detail. For Example if user want to search Special species of Animal from image we need to train model which analyze model in more detail are given best result to user. There are many ways to process the image globally used. There are some tech giant companies like Google, Facebook, Amazon are working on this project increase user search accuracy</p>


![image](https://user-images.githubusercontent.com/28058334/175197605-3eb94bd2-9751-4166-9669-50944808ccd4.png)


<h2>Purpose of the project</h2><br/>
<p>The purpose of the project is the allow user to search the data from dataset by using content not by using name or tags. Now a Days, this topic is very hot as we discuss before everyone try to increase accuracy of content matching. They are try many different methods for achieve the goals. Some people try to extract feature and save it in single file and when user search image it match values and return the links.</p>

<h2>Methodology</h2><br/>
<p>This project is based on many different framework. We are using some of following framework in this project. We use Tansorflow Keras for extracting features of image. And Flask server for webpage for interact with system.</p>

<h2>This Project have two phases</h2> <br/>
<ol>
    <li> Dataset Feature Extraction</li>
    <li> Search</li>
</ol>
 
<h2>Dataset Feature Extraction</h2>
<p>In this phase we train model in following hierarchy. In this process user give dataset to Model for Extract the features from image dataset any save it into feature folder in “.npy” format.</p>

![image](https://user-images.githubusercontent.com/28058334/175197775-45ea3b2c-1fc1-412d-9594-b87b106bdd09.png)









<br><br><br><br>
<h2>Step of installation</h2>
<ol>
    <li>Open project in visual studio code</li>
    <li>Open terminal</li>
    <li>Enter following command
        <ol>
             <li> pip install -r dependencies.txt</li>
             <li>  python featureExtractor.py</li>
             <li> Run: http://127.0.0.1:5000/ on browser</li>
        </ol>
    </li>
</ol>
