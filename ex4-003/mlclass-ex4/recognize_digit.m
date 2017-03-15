%% Initialization
clear ; close all; clc

%% Setup the parameters you will use for this exercise
input_layer_size  = 400;  % 20x20 Input Images of Digits
hidden_layer_size = 25;   % 25 hidden units
num_labels = 10;          % 10 labels, from 1 to 10   
                          % (note that we have mapped "0" to label 10)

%% =========== Part 1: Loading and Visualizing Data =============
%  We start the exercise by first loading and visualizing the dataset. 
%  You will be working with a dataset that contains handwritten digits.
%

% Load Training Data
%fprintf('Loading Data...\n')
load('ex4data1.mat');
m = size(X, 1);

%% ================ Part 2: Loading Parameters ================
% In this part of the exercise, we load some pre-initialized 
% neural network parameters.

%fprintf('Loading Saved Neural Network Parameters...\n')

% Load the weights into variables Theta1 and Theta2
load('ex4weights.mat');

% Unroll parameters ''
%nn_params = [Theta1(:) ; Theta2(:)];


%% ================= Part 10: Implement Predict =================
%  After training the neural network, we would like to use it to predict
%  the labels. You will now implement the "predict" function to use the
%  neural network to predict the labels of the training set. This lets
%  you compute the training set accuracy.

%idx = 1001;
%in = X(idx,:);
%out = y(idx);

%in
%out
paint_data;

pred = predict(Theta1, Theta2, digit);
fprintf('%d\n', pred);

%fprintf('Training Set Accuracy: %f\n', mean(double(pred == y)) * 100);


