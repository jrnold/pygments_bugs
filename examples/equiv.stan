# Equiv: bioequivalence in a cross-over trial
#  http://www.openbugs.info/Examples/Equiv.html

data {
  int(0,) P; 
  int(0,) N; 
  int group[N]; 
  real Y[N, P]; 
  int sign[2];
} 

transformed data {
  int T[N, P]; 
  for (n in 1:N) 
    for (p in 1:P) 
      T[n,p] <- (group[n] * (2 * p - 3) + 3) / 2;
} 

parameters {
  real mu;
  real phi; 
  real pi; 
  real(0,) sigmasq1;
  real(0,) sigmasq2;
  real delta[N]; 
} 

transformed parameters {
  real sigma1;
  real sigma2;
  sigma1 <- sqrt(sigmasq1); 
  sigma2 <- sqrt(sigmasq2); 
} 

model {
  for (p in 1:P) {
    for (n in 1:N) {
      Y[n, p] ~ normal(mu + sign[T[n, p]] * phi / 2 + sign[p] * pi / 2 + delta[n], sigma1); 
    }
  }
  delta ~ normal(0, sigma2); 
  sigmasq1 ~ inv_gamma(.001, .001); 
  sigmasq2 ~ inv_gamma(.001, .001); 
  mu ~ normal(0.0, 1000); 
  phi ~ normal(0.0, 1000); 
  pi ~ normal(0.0, 1000); 
}

generated quantities {
  real equiv;
  real theta;

  theta <- exp(phi);
  equiv <- step(theta - 0.8) -
           step(theta - 1.2);
}