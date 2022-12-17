#include <cmath>

float DeltaEta(const float& eta1, const float& eta2)
{
  return fabs( eta1 - eta2 );
}

float DeltaPhi(const float& phi1, const float& phi2)
{
  float dphi = fabs( phi1 - phi2 );
  if( dphi > M_PI ) dphi = 2*M_PI - dphi;
  return dphi;
}

float DeltaR(double eta1=0, double phi1=0,
             double eta2=0, double phi2=0)
{
  return sqrt( DeltaEta(eta1,eta2)*DeltaEta(eta1,eta2) + 
               DeltaPhi(phi1,phi2)*DeltaPhi(phi1,phi2) );
}

double DeltaRmin(double etaph1=0, double phiph1=0, double etaph2=0, double phiph2=0, double etaj1=0, double phij1=0,double etaj2=0, double phij2=0)
{

  return min( 
	     DeltaR(etaph1, phiph1, etaj1, phij1), min( 
	       DeltaR(etaph1, phiph1, etaj2, phij2), min(
  		  DeltaR(etaph2, phiph2, etaj1, phij1), DeltaR(etaph2, phiph2, etaj2, phij2))));
}

double otherDeltaR(double etaph1=0, double phiph1=0, double etaph2=0, double phiph2=0, double etaj1=0, double phij1=0,double etaj2=0, double phij2=0)
{
  double dRmin = DeltaRmin(etaph1, phiph1, etaph2, phiph2, etaj1, phij1,etaj2, phij2);

  if( DeltaR(etaph1, phiph1, etaj1, phij1)==dRmin )
    return DeltaR(etaph2, phiph2, etaj2, phij2);

  if( DeltaR(etaph1, phiph1, etaj2, phij2)==dRmin )
    return DeltaR(etaph2, phiph2, etaj1, phij1);

  if( DeltaR(etaph2, phiph2, etaj1, phij1)==dRmin )
    return DeltaR(etaph1, phiph1, etaj2, phij2);

  if( DeltaR(etaph2, phiph2, etaj2, phij2)==dRmin )
    return DeltaR(etaph1, phiph1, etaj1, phij1);

  return 0;
}
