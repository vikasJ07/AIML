import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

iris=datasets.load_iris()
x=iris.data
y=iris.target
class_names=iris.target_names

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.2,random_state=42)

class Naive:
    def __init__(self,x,y):
        n_samples,n_features=x.shape
        self.classes=np.unique(y)
        n_classes=len(self.classes)
        
        self.means=np.zeros((n_classes,n_features))
        self.vars=np.zeros((n_classes,n_features))
        self.priors=np.zeros(n_classes)
        
        for i in range(n_classes):
            c=self.classes[i]
            x_c=x[y==c]
            self.means[i:]=x_c.mean(axis=0)
            self.vars[i:]=x_c.var(axis=0)
            self.priors[i]=x_c.shape[0]/x.shape[0]
            
    def prediction(self,x):
        posteriors=[]
        for i in range(len(self.classes)):
            c=self.classes[i]
            prior=np.log(self.priors[i])
            class_cond=np.sum(np.log(self.pdf(x,i)))
            posterior=prior+class_cond
            posteriors.append(posterior)
        return self.classes[np.argmax(posteriors)]
    
    def predict(self,X):
        return [self.prediction(x) for x in X]
    
    def pdf(self,x,i):
        mean=self.means[i]
        var=self.vars[i]
        numerator=np.exp(-((x-mean)**2)/(2*var))
        denominator=np.sqrt(2*np.pi*var)
        return numerator/denominator
    

nb=Naive(x_train,y_train)
x_train.shape,y_train.shape

y_pred=nb.predict(x_test)
np.mean(y_pred==y_test)

accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy}")



print("\nConfusion Matrix:",confusion_matrix(y_test, y_pred))


print("\nClassification Report:",classification_report(y_test, y_pred, target_names=class_names))