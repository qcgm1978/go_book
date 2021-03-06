#!/usr/bin/env python
# coding: utf-8

# ### App B.The backpropagation algorithm
# 
# Chapter 5 introduced sequential neural networks and feed-forward networks in particular. We briefly talked about the __backpropagation algorithm__, which is used to train neural networks. This appendix explains in a bit more detail how to arrive at the gradients and parameter updates that we simply stated and used in chapter 5.
# 
# We’ll first derive the backpropagation algorithm for feed-forward neural networks and then discuss how to extend the algorithm to more-general sequential and nonsequential networks. Before going deeper into the math, let’s define our setup and introduce notation that will help along the way.
# #### A bit of notation

# In this section, you’ll work with a feed-forward neural network with ${l} $ layers. Each of the ${l}$ layers has a sigmoid activation function. Weights of the ${i}$ th layer are referred to as ${W^i}$ , and bias terms by $b^i$ . You use $x$ to denote a mini-batch of size $k$ of input data to the network, and $y$ to indicate the output of it. It’s safe to think of both $x$ and $y$ as vectors here, but all operations carry over to mini-batches. Moreover, we introduce the following notation:

# - We indicate the output of the $i$ th layer with activation $y^{i+1}$ ; that is, $y^{i+1} = s(W^iy^i + b^i$ ). Note that $y^{i+1}$ is also the __input__ to layer $i +1$.
# 
# - We indicate the output of the _i_ th dense layer without activation as $z^i$; that is, $z^i = W^i · y^i + b^i$.
# 
# - Introducing this convenient way of writing intermediate output, you can now write $z^i = W^i · y^i + b^i$ and $y^{i+1} = s(z^i)$. Note that with this notation, you could also write the output as $y = y^l$ and the input as $x = y^0$, but we won’t use this notation in what follows.
# 
# - As a last piece of notation, we’ll sometimes write $f^i(y^i)$ for $s(W^iy^i + b^i)$.
# 

# 

# #### __The backpropagation algorithm for feed-forward networks__
# Following the preceding conventions, the forward pass for the ith layer of your neural network can now be written as follows:
# 
# $y^{i+1} = σ(W^iy^i + b^i) = f^i \: o \: y^i$
# 
# You can use this definition recursively for each layer to write your predictions like this:
# 
# $y = f^n o ··· o f^1(x)$
# 
# Because you compute your loss function __Loss__ from predictions __y__ and labels __ŷ__, you can split the loss function in a similar fashion:
# 
# $Loss(y,ŷ) = Loss \: o \: f^n o ··· o f^1(x)$

# Computing and using the derivative of the loss function as shown here is done by a smart application of the **chain rule** for functions, a fundamental result from multivariable calculus. Directly applying the chain rule to the preceding formula yields this:
# $ 
#     \frac{dLoss}{dx}=\frac{dLoss}{df^n}·\frac{df^n}{df^{n-1}}···\frac{df^2}{df^1}·\frac{df^1}{dx}$
# Now, you define the delta of the _i_ th layer as follows:
# 
# $\Delta^i=\frac{dLoss}{df^n}···\frac{df^{i+1}}{df^i}$
# 
# Then you can express deltas in a similar fashion to the previous __forward pass__, which you call the backward pass—namely, by the following relationship:
# 
# $
#     \Delta^i=\Delta^{i+1}\frac{df^{i+1}}{df^i}$
# Note that for deltas, the indices go down, as you pass backward through the computation. Formally, computing the backward pass is structurally equivalent to the simple forward pass. You’ll now proceed to explicitly computing the actual derivatives involved. Derivatives of both sigmoid and affine linear functions with respect to their input are quickly derived:
# 
# $
#     \omicron^`(x)=\frac{d\omicron}{dx}=\omicron(x)(1-\omicron(x)) $
# $
#     \frac{d(Wx+b)}{dx}=W$
# Using these last two equations, you can now write down how to propagate back the error term $D^{i+1}$ of the (_i + 1_)th layer to the _i_ th layer:
# 
# $\Delta^i=(W^i)^T·(\Delta^{i+1}) \: \odot \: \omicron^`(z^i))$
# 
# In this formula, the superscript T denotes matrix transposition. The ⊙, or __Hadamard product__, indicates element-wise multiplication of the two vectors. The preceding computation splits into two parts, one for the dense layer and one for the activation:
# 
# $\Delta^i=(w^i)^T·(\Delta^{i+1})\odot\omicron^`(z^i)\Delta^i=(W^i)^T·\Delta^\omicron$
# 
# The last step is to compute the gradients of your parameters Wi and bi for every layer. Now that you have Di readily computed, you can immediately read off parameter gradients from there:
# 
# $
#     \Delta W^i=\frac{dLoss}{dW^i}=\Delta^i·(y^i)^\Tau$
# $
# \Delta b^i=\frac{dLoss}{db^i}=\Delta^i$
# 
# With these error terms, you can update your neural network parameters as you wish, meaning with any optimizer or update rule you like.
# 
# 
# 

# ###   Backpropagation for sequential neural networks
# In general, sequential neural networks can have more-interesting layers than what we’ve discussed so far. For instance, you could be concerned with convolutional layers, as described in [chapter 6](https://livebook.manning.com/book/deep-learning-and-the-game-of-go/chapter-6/ch06), or other activation functions, such as the softmax activation discussed in chapter 6 as well. Regardless of the actual layers in a sequential network, backpropagation follows the same general outline. If ${g^i}$ denotes the forward pass without activation, and ${Act^i}$ denotes the respective activation function, propagating $Δ^{i+1}$ to the _i_ th layer requires you to compute the following transition:
# 
# $
#     \Delta^i=\frac{dAct^i}{dg^i}(z^i)\frac{dg^i}{dz^i}(y^i)\Delta^{i+1}$
# You need to compute the derivative of the activation function evaluated at the intermediate output $z^i$ and the derivative of the layer function $g^i$ with respect to the input of the _i_ th layer. Knowing all the deltas, you can usually quickly deduce gradients for all parameters involved in the layer, just as you did for weights and bias terms in the feed-forward layer. Seen this way, each layer knows how to pass data forward and propagate an error backward, without explicitly knowing anything about the structure of the surrounding layers.
# 
# 

# ### Backpropagation for neural networks in general
# 
# In this book, we’re concerned solely with sequential neural networks, but it’s still interesting to discuss what happens when you move away from the sequentiality constraint. In a nonsequential network, a layer has multiple outputs, multiple inputs, or both.
# 
# Let’s say a layer has __m__ outputs. A prototypical example might be to split up a vector into __m__ parts. Locally for this layer, the forward pass can be split into __k separate__ functions. On the backward pass, the derivative of each of these functions can be computed separately as well, and each derivative contributes equally to the delta that’s being passed on to the previous layer.
# 
# In the situation that we have to deal with, __n__ inputs and one output, the situation is somewhat reversed. The forward pass is computed from __n__ input components by means of a single function that outputs a single value. On the backward pass, you receive one delta from the next layer and have to compute __n__ output deltas to pass on to each one of the incoming __n__ layers. Those derivatives can be computed independently of each other, evaluated at each of the respective inputs.
# 
# The general case of __n__ inputs and __m__ outputs works by combining the two previous steps. Each neural network, no matter how complicated the setup or how many layers in total, locally looks like this.
# 
# 
# 
# 

# ### Computational challenges with backpropagation
# 
# You could argue that backpropagation is just a simple application of the chain rule to a specific class of machine-learning algorithms. Although on a theoretical level it may be seen like this, in practice there’s a lot to consider when implementing backpropagation.
# 
# Most notably, to compute deltas and gradient updates for any layer, you have to have the respective inputs of the forward pass ready for evaluation. If you simply discard results from the forward pass, you have to recompute them on the backward pass. Thus, you’d do well by caching those values in an efficient way. In your implementation from scratch in chapter 5, each layer persisted its own state, for input and output data, as well as for input and output deltas. Building networks that rely on processing massive amounts of data, you should make sure to have an implementation in place that’s both computationally efficient and has a low memory footprint.
# 
# Another related, interesting consideration is that of reusing intermediate values. For instance, we’ve argued that in the simple case of a feed-forward network, we can either see affine linear transformation and sigmoid activation as a unit or split them into two layers. The output of the affine linear transformation is needed to compute the backward pass of the activation function, so you should keep that intermediate information from the forward pass. On the other hand, because the sigmoid function doesn’t have parameters, you compute the backward pass in one go:
# 
# $\Delta^i=(W^i)^T(\Delta^{i+1} \odot (z^i))$
# 
# This might computationally be more efficient than doing it in two steps. Automatically detecting which operations can be carried out together can bring a lot of speed gains. In more-complicated situations (such as that of recurrent neural networks, in which a layer will essentially compute a __loop__ with inputs from the last step), managing intermediate state becomes even more important.
# 
# 
