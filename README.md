# sensa
  Senas is  free sentiment analysis tool is based on the most recent Deep learning algorithms.

  The goal of this project is to be able to consistently detect emotions in normal conversational sentences , help businesses monitor brand and product sentiment in customer feedback, and understand customer needs.

  In this work, Bi Long Short-Term Memory (BILSTM) as a deep neural network has been used for training a model after features that extract automatically from input texts by a word embedding method as a first hidden layer(BILSTM layer), then softMax layer is applied to turn numeric outputs from LSTM layer into probabilities to classify the outputs to : (joy ,sadness anger ,fear ,love ,surprise ).
  

![Screenshot__110_-removebg-preview (1)](https://user-images.githubusercontent.com/57809558/177050017-8295be97-85c0-4c31-8d3b-364a9c9da38f.png)

  Finally, the performance of the proposed model is evaluated via experimentson public dataset that is List of documents with emotion flag, It is split into train, test & validation for building the machine learning model, It helps greatly in NLP Classification tasks . 
  Results shown in model accuracy graph and Confusion matrix shown below
  
  ![image](https://user-images.githubusercontent.com/57809558/177051205-4ba08134-ce97-4215-b1c3-f12fe546de0a.png)


Flask as lightweight Python web framework has been used for creating web application to make this model available anywhere and for everyone in user-friendly simple interface.



