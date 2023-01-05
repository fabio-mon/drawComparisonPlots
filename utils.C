#include <cmath>
#include "TLorentzVector.h"

//dummy function with the same name of the macro required by root
float utils()
{
  return 0.;
}
/*
float HHPt(TLorentzVector h1, TLorentzVector h2)
{
  return (h1+h2).Pt();
}
*/
float HHPt(float pt1, float eta1, float phi1, float m1, float pt2, float eta2, float phi2, float m2)
{
  TLorentzVector h1, h2;
  h1.SetPtEtaPhiM(pt1,eta1,phi1,m1);
  h2.SetPtEtaPhiM(pt2,eta2,phi2,m2);
  return (h1+h2).Pt();
}

float HHmass(float pt1, float eta1, float phi1, float m1, float pt2, float eta2, float phi2, float m2)
{
  TLorentzVector h1, h2;
  h1.SetPtEtaPhiM(pt1,eta1,phi1,m1);
  h2.SetPtEtaPhiM(pt2,eta2,phi2,m2);
  return (h1+h2).M();
}
