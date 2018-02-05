#! /usr/bin/python
#-*-coding:utf-8 -*-

import pandas as pd
import numpy as np
import tensorflow as tf


data_path = "..\\mydata\\car.csv"
col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
data = pd.read_csv(data_path,names =  col_names)
# use onehot to encode the data
data_1 = pd.get_dummies(data,prefix=list(data.columns));


data_1 = data_1.values.astype(np.float32)
np.random.shuffle(data_1)
sep = int(0.7*len(data_1))
train_data = data_1[:sep]
test_data =  data_1[sep:]

tf_input = tf.placeholder(tf.float32,[None,25],"input")
tfx = tf_input[:,:21]
tfy = tf_input[:,21:]

l1 = tf.layers.dense(tfx,128,tf.nn.relu,name='l1')
l2 = tf.layers.dense(l1,128,tf.nn.relu,name='l2')
out = tf.layers.dense(l2,4,name='l3')
prediction = tf.nn.softmax(out,name='pred')

loss = tf.losses.softmax_cross_entropy(onehot_labels=tfy,logits=out)
accuracy = tf.metrics.accuracy(labels=tf.argmax(tfy,axis=1),predictions=tf.argmax(out,axis=1))[1]
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_opt = opt.minimize(loss)

sess = tf.Session()
sess.run(tf.group(tf.global_variables_initializer(),tf.local_variables_initializer()))

for i in range(4000):
    batch_index = np.random.randint(len(train_data),size=32)
    sess.run(train_opt,{tf_input:train_data[batch_index]})

    if i%50 == 0:
        acc_,pred_,loss_ = sess.run([accuracy,prediction,loss],{tf_input:test_data})
        print("Step:%i" % i,"|Accurate:%.2f"%acc_,"|Loss:%.2f"% loss_)






