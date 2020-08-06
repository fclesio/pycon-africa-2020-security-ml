# PyCon Africa 2020 - Security in Machine Learning: Adversarial attacks, model failures and countermeasures

This repo brings the code related with the talk [Security in Machine Learning: Adversarial attacks, model failures and countermeasures that was given in the PyCon Africa 2020](https://africa.pycon.org/speakers/flavio-clesio).

The [slide deck](https://speakerdeck.com/fclesio/security-in-machine-learning) contains all the references and more cases


## Demo Summary

- [Attacking ML Supply Chain](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/attacking-ml-supply-chain): _Owing to large resources (data + computation) required to train algorithms, the current practice is to reuse models trained by large corporations, and modify them slightly for task at hand (e.g: ResNet is a popular image recognition model from Microsoft). These models are curated ina Model Zoo (Caffe hosts popular image recognition models). In this attack,the adversary attacks the models hosted in Caffe, thereby poisoning the well for anyone else[1]._

- [Membership Inference](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/membership-inference): _The attacker can determine whether a given data record was part of the model’s training dataset or not_[1]

- [Model Backdooring](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/model-backdoor): _Like in the “Attacking the ML Supply Chain”, In this attack scenario,the training process is either fully or partially outsourced to a malicious party who wants to provide the user with a trained model that contains a backdoor. The backdoored model would perform well on most inputs (including inputs that the end user may hold out as a validation set) but cause targeted misclassifications or degrade the accuracy of the model for inputs that satisfy some secret, attacker-chosen property, which we will refer to as the backdoor trigger_[1]

- [Model Inversion](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/model-inversion): _Attacker recovers the secret features used in the model by through careful queries_[1]

- [Model Poisoning](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/model-poisoning): _The goal of the attacker is to contaminate the machine model generated in the training phase, so that predictions on new data will be modified in the testing phase_[1]

- [Model Stealing](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/model-stealing): _The attackers recreate the underlying model by legitimately querying the model. The functionality of the new model is same as that of the underlying model._[1]



## References
[1] - [Kumar, Ram Shankar Siva, et al. "Failure modes in machine learning systems." arXiv preprint arXiv:1911.11034 (2019).](https://arxiv.org/abs/1911.11034)
