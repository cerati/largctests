import ROOT as r

f = r.TFile.Open("/uboone/data/users/cerati/fittedvertexntuplewithinput_bnb_nu_cosmic_mcc8.4_reco2_sipcut_v3.root","READ")

r.gStyle.SetOptStat(0)
r.gStyle.SetHistLineWidth(2)

c1 = r.TCanvas("c1","c1",800,800)
pn_CountValidPoints = f.Get("trackingperformancePN/CountValidPoints")
kt_CountValidPoints = f.Get("trackingperformancePNKT/CountValidPoints") 
in_CountValidPoints = f.Get("trackingperformance/CountValidPoints") 
pn_CountValidPoints.SetLineColor(r.kRed)
kt_CountValidPoints.SetLineColor(r.kBlue)
in_CountValidPoints.SetLineColor(r.kBlack)
pn_CountValidPoints.GetXaxis().SetTitle("N Valid Points")
pn_CountValidPoints.Draw()
kt_CountValidPoints.Draw("same")
in_CountValidPoints.Draw("same")
c1.SaveAs("CountValidPoints.png")

c2 = r.TCanvas("c2","c2",800,800)
pn_dLengthRel = f.Get("trackingperformancePN/dLengthRel") 
kt_dLengthRel = f.Get("trackingperformancePNKT/dLengthRel") 
in_dLengthRel = f.Get("trackingperformance/dLengthRel") 
pn_dLengthRel.SetLineColor(r.kRed)
kt_dLengthRel.SetLineColor(r.kBlue)
in_dLengthRel.SetLineColor(r.kBlack)
pn_dLengthRel.SetLineWidth(2)
kt_dLengthRel.SetLineWidth(2)
in_dLengthRel.SetLineWidth(2)
pn_dLengthRel.GetXaxis().SetTitle("(L_{rec}-L_{MC})/L_{MC}")
pn_dLengthRel.Draw()
kt_dLengthRel.Draw("same")
in_dLengthRel.Draw("same")
c2.SaveAs("dLengthRel.png")

c22 = r.TCanvas("c22","c22",800,800)
pn_dotpdir = f.Get("trackingperformancePN/dotpdir") 
kt_dotpdir = f.Get("trackingperformancePNKT/dotpdir") 
in_dotpdir = f.Get("trackingperformance/dotpdir") 
pn_dotpdir.SetLineColor(r.kRed)
kt_dotpdir.SetLineColor(r.kBlue)
in_dotpdir.SetLineColor(r.kBlack)
pn_dotpdir.GetXaxis().SetTitle("#vec{U_{rec}} #upoint #vec{U_{MC}}")
pn_dotpdir.Draw()
kt_dotpdir.Draw("same")
in_dotpdir.Draw("same")
c22.SaveAs("dotpdir.png")

c3 = r.TCanvas("c3","c3",1800,600)
c3.Divide(3,1)
c3.cd(1)
pn_dx_prop_assoc = f.Get("trackingperformancePN/dx_prop_assoc") 
kt_dx_prop_assoc = f.Get("trackingperformancePNKT/dx_prop_assoc") 
in_dx_prop_assoc = f.Get("trackingperformance/dx_prop_assoc") 
pn_dx_prop_assoc.SetLineColor(r.kRed)
kt_dx_prop_assoc.SetLineColor(r.kBlue)
in_dx_prop_assoc.SetLineColor(r.kBlack)
in_dx_prop_assoc.GetXaxis().SetTitle("(x_{rec}-x_{MC}) [cm]")
in_dx_prop_assoc.Draw()
kt_dx_prop_assoc.Draw("same")
pn_dx_prop_assoc.Draw("same")
c3.cd(2)
pn_dy_prop_assoc = f.Get("trackingperformancePN/dy_prop_assoc") 
kt_dy_prop_assoc = f.Get("trackingperformancePNKT/dy_prop_assoc") 
in_dy_prop_assoc = f.Get("trackingperformance/dy_prop_assoc") 
pn_dy_prop_assoc.SetLineColor(r.kRed)
kt_dy_prop_assoc.SetLineColor(r.kBlue)
in_dy_prop_assoc.SetLineColor(r.kBlack)
in_dy_prop_assoc.GetXaxis().SetTitle("(y_{rec}-y_{MC}) [cm]")
in_dy_prop_assoc.Draw()
kt_dy_prop_assoc.Draw("same")
pn_dy_prop_assoc.Draw("same")
c3.cd(3)
pn_dz_prop_assoc = f.Get("trackingperformancePN/dz_prop_assoc") 
kt_dz_prop_assoc = f.Get("trackingperformancePNKT/dz_prop_assoc") 
in_dz_prop_assoc = f.Get("trackingperformance/dz_prop_assoc") 
pn_dz_prop_assoc.SetLineColor(r.kRed)
kt_dz_prop_assoc.SetLineColor(r.kBlue)
in_dz_prop_assoc.SetLineColor(r.kBlack)
in_dz_prop_assoc.GetXaxis().SetTitle("(z_{rec}-z_{MC}) [cm]")
in_dz_prop_assoc.Draw()
kt_dz_prop_assoc.Draw("same")
pn_dz_prop_assoc.Draw("same")
c3.SaveAs("dpos_prop_assoc.png")

c4 = r.TCanvas("c4","c4",1800,600)
c4.Divide(3,1)
c4.cd(1)
pn_dux_prop_assoc = f.Get("trackingperformancePN/dux_prop_assoc") 
kt_dux_prop_assoc = f.Get("trackingperformancePNKT/dux_prop_assoc") 
in_dux_prop_assoc = f.Get("trackingperformance/dux_prop_assoc") 
pn_dux_prop_assoc.SetLineColor(r.kRed)
kt_dux_prop_assoc.SetLineColor(r.kBlue)
in_dux_prop_assoc.SetLineColor(r.kBlack)
in_dux_prop_assoc.GetXaxis().SetTitle("(ux_{rec}-ux_{MC})")
in_dux_prop_assoc.Draw()
kt_dux_prop_assoc.Draw("same")
pn_dux_prop_assoc.Draw("same")
c4.cd(2)
pn_duy_prop_assoc = f.Get("trackingperformancePN/duy_prop_assoc") 
kt_duy_prop_assoc = f.Get("trackingperformancePNKT/duy_prop_assoc") 
in_duy_prop_assoc = f.Get("trackingperformance/duy_prop_assoc") 
pn_duy_prop_assoc.SetLineColor(r.kRed)
kt_duy_prop_assoc.SetLineColor(r.kBlue)
in_duy_prop_assoc.SetLineColor(r.kBlack)
in_duy_prop_assoc.GetXaxis().SetTitle("(uy_{rec}-uy_{MC})")
in_duy_prop_assoc.Draw()
kt_duy_prop_assoc.Draw("same")
pn_duy_prop_assoc.Draw("same")
c4.cd(3)
pn_duz_prop_assoc = f.Get("trackingperformancePN/duz_prop_assoc") 
kt_duz_prop_assoc = f.Get("trackingperformancePNKT/duz_prop_assoc") 
in_duz_prop_assoc = f.Get("trackingperformance/duz_prop_assoc") 
pn_duz_prop_assoc.SetLineColor(r.kRed)
kt_duz_prop_assoc.SetLineColor(r.kBlue)
in_duz_prop_assoc.SetLineColor(r.kBlack)
in_duz_prop_assoc.GetXaxis().SetTitle("(uz_{rec}-uz_{MC})")
in_duz_prop_assoc.Draw()
kt_duz_prop_assoc.Draw("same")
pn_duz_prop_assoc.Draw("same")
c4.SaveAs("ddir_prop_assoc.png")

c5 = r.TCanvas("c5","c5",800,800)
pn_mu_mcsmom_vs_truemom = f.Get("trackingperformancePN/mu_mcsmom_vs_truemom") 
pn_mu_mcsmom_vs_truemom.GetXaxis().SetTitle("True momentum [GeV]")
pn_mu_mcsmom_vs_truemom.GetYaxis().SetTitle("MCS fit momentum [GeV]")
pn_mu_mcsmom_vs_truemom.Draw("colz")
c5.SaveAs("mu_mcsmom_vs_truemom.png")

c6 = r.TCanvas("c6","c6",800,800)
pn_mu_mcsmom_vs_truemom_contained = f.Get("trackingperformancePN/mu_mcsmom_vs_truemom_contained") 
pn_mu_mcsmom_vs_truemom_contained.GetXaxis().SetTitle("True momentum [GeV]")
pn_mu_mcsmom_vs_truemom_contained.GetYaxis().SetTitle("MCS fit momentum [GeV]")
pn_mu_mcsmom_vs_truemom_contained.Draw("colz")
c6.SaveAs("mu_mcsmom_vs_truemom_contained.png")

c7 = r.TCanvas("c7","c7",1800,600)
c7.Divide(3,1)
c7.cd(1)
kt_dx_pull_prop_assoc = f.Get("trackingperformancePNKT/dx_pull_prop_assoc") 
kt_dx_pull_prop_assoc.SetLineColor(r.kBlue)
kt_dx_pull_prop_assoc.GetXaxis().SetTitle("(x_{rec}-x_{MC})/#sigma_{x}")
kt_dx_pull_prop_assoc.Draw()
c7.cd(2)
kt_dy_pull_prop_assoc = f.Get("trackingperformancePNKT/dy_pull_prop_assoc") 
kt_dy_pull_prop_assoc.SetLineColor(r.kBlue)
kt_dy_pull_prop_assoc.GetXaxis().SetTitle("(y_{rec}-y_{MC})/#sigma_{y}")
kt_dy_pull_prop_assoc.Draw()
c7.cd(3)
kt_dz_pull_prop_assoc = f.Get("trackingperformancePNKT/dz_pull_prop_assoc") 
kt_dz_pull_prop_assoc.SetLineColor(r.kBlue)
kt_dz_pull_prop_assoc.GetXaxis().SetTitle("(z_{rec}-z_{MC})/#sigma_{z}")
kt_dz_pull_prop_assoc.Draw()
c7.SaveAs("dpos_pull_prop_assoc.png")

c8 = r.TCanvas("c8","c8",1800,600)
c8.Divide(3,1)
c8.cd(1)
kt_dux_pull_prop_assoc = f.Get("trackingperformancePNKT/dux_pull_prop_assoc") 
kt_dux_pull_prop_assoc.SetLineColor(r.kBlue)
kt_dux_pull_prop_assoc.GetXaxis().SetTitle("(ux_{rec}-ux_{MC})/#sigma_{ux}")
kt_dux_pull_prop_assoc.Draw()
c8.cd(2)
kt_duy_pull_prop_assoc = f.Get("trackingperformancePNKT/duy_pull_prop_assoc") 
kt_duy_pull_prop_assoc.SetLineColor(r.kBlue)
kt_duy_pull_prop_assoc.GetXaxis().SetTitle("(uy_{rec}-uy_{MC})/#sigma_{uy}")
kt_duy_pull_prop_assoc.Draw()
c8.cd(3)
kt_duz_pull_prop_assoc = f.Get("trackingperformancePNKT/duz_pull_prop_assoc") 
kt_duz_pull_prop_assoc.SetLineColor(r.kBlue)
kt_duz_pull_prop_assoc.GetXaxis().SetTitle("(uz_{rec}-uz_{MC})/#sigma_{uz}")
kt_duz_pull_prop_assoc.Draw()
c8.SaveAs("ddir_pull_prop_assoc.png")

c72 = r.TCanvas("c72","c72",1800,600)
c72.Divide(3,1)
c72.cd(1)
in_dx_pull_prop_assoc = f.Get("trackingperformance/dx_pull_prop_assoc") 
in_dx_pull_prop_assoc.SetLineColor(r.kBlack)
in_dx_pull_prop_assoc.GetXaxis().SetTitle("(x_{rec}-x_{MC})/#sigma_{x}")
in_dx_pull_prop_assoc.Draw()
c72.cd(2)
in_dy_pull_prop_assoc = f.Get("trackingperformance/dy_pull_prop_assoc") 
in_dy_pull_prop_assoc.SetLineColor(r.kBlack)
in_dy_pull_prop_assoc.GetXaxis().SetTitle("(y_{rec}-y_{MC})/#sigma_{y}")
in_dy_pull_prop_assoc.Draw()
c72.cd(3)
in_dz_pull_prop_assoc = f.Get("trackingperformance/dz_pull_prop_assoc") 
in_dz_pull_prop_assoc.SetLineColor(r.kBlack)
in_dz_pull_prop_assoc.GetXaxis().SetTitle("(z_{rec}-z_{MC})/#sigma_{z}")
in_dz_pull_prop_assoc.Draw()
c72.SaveAs("in_dpos_pull_prop_assoc.png")

c82 = r.TCanvas("c82","c82",1800,600)
c82.Divide(3,1)
c82.cd(1)
in_dux_pull_prop_assoc = f.Get("trackingperformance/dux_pull_prop_assoc") 
in_dux_pull_prop_assoc.SetLineColor(r.kBlack)
in_dux_pull_prop_assoc.GetXaxis().SetTitle("(ux_{rec}-ux_{MC})/#sigma_{ux}")
in_dux_pull_prop_assoc.Draw()
c82.cd(2)
in_duy_pull_prop_assoc = f.Get("trackingperformance/duy_pull_prop_assoc") 
in_duy_pull_prop_assoc.SetLineColor(r.kBlack)
in_duy_pull_prop_assoc.GetXaxis().SetTitle("(uy_{rec}-uy_{MC})/#sigma_{uy}")
in_duy_pull_prop_assoc.Draw()
c82.cd(3)
in_duz_pull_prop_assoc = f.Get("trackingperformance/duz_pull_prop_assoc") 
in_duz_pull_prop_assoc.SetLineColor(r.kBlack)
in_duz_pull_prop_assoc.GetXaxis().SetTitle("(uz_{rec}-uz_{MC})/#sigma_{uz}")
in_duz_pull_prop_assoc.Draw()
c82.SaveAs("in_ddir_pull_prop_assoc.png")

c9 = r.TCanvas("c9","c9",800,800)
in_ptype_rec_vs_mc = f.Get("trackingperformance/ptype_rec_vs_mc") 
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(1,"unset")
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(2,"muon")
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(3,"pion")
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(4,"kaon")
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(5,"proton")
in_ptype_rec_vs_mc.GetXaxis().SetBinLabel(6,"electron")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(1,"unset")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(2,"muon")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(3,"pion")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(4,"kaon")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(5,"proton")
in_ptype_rec_vs_mc.GetYaxis().SetBinLabel(6,"electron")
in_ptype_rec_vs_mc.GetXaxis().SetTitle("True particle ID")
in_ptype_rec_vs_mc.GetYaxis().SetTitle("Reco particle ID")
in_ptype_rec_vs_mc.GetYaxis().SetTitleOffset(1.0)
in_ptype_rec_vs_mc.LabelsOption("h","Y")
in_ptype_rec_vs_mc.Draw("colz, text")
c9.SaveAs("ptype_rec_vs_mc.png")

c10 = r.TCanvas("c10","c10",800,800)
in_deltaPrel_okid = f.Get("trackingperformance/deltaPrel_okid") 
in_deltaPrel_okid.SetLineColor(r.kBlack)
in_deltaPrel_okid.GetXaxis().SetTitle("(P_{rec}-P_{MC})/P_{MC}")
in_deltaPrel_okid.Draw()
c10.SaveAs("deltaPrel_okid.png")