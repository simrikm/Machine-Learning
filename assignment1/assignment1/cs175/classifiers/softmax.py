import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in xrange(num_train):
    scores = X[i].dot(W)
    scores_exp=np.exp(scores[y[i]])
    scores_expsum=np.sum(np.exp(scores))
    loss+=-np.log(scores_exp/scores_expsum)
    for j in xrange(num_classes):
      if j == y[i]:
        dW[:,j]+=((np.exp(scores[j])/scores_expsum)-1)*X[i]
      else:
        dW[:,j]+=np.exp(scores[j])/scores_expsum*X[i]
            
  loss /= num_train
  dW/=num_train
  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  dW+=reg*W


  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train=X.shape[0]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores= X.dot(W)
  exp_score=np.exp(scores)
  sum_score = np.sum(np.exp(scores),axis=1,keepdims=True)
  h =exp_score/sum_score

  loss = np.sum(-np.log(h[np.arange(num_train), y]))
  loss/=num_train
  loss+=reg*np.sum(W*W)
    
  #indicator=np.zeros(margins.shape)
  h[np.arange(num_train),y]+=-1
  dW = X.T.dot(h)
  dW/=num_train
  dW+=reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

