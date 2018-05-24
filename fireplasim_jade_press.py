import numpy as np

if __name__=="__main__":
        header = "# PID MODEL JOBNAME STATUS NCORES QUEUE nfixorb eccen obliq vernlon lockedyear year naqua pCO2 pressure flux script extra notify alloutput keeprestart restart"

	tstr1 = " 0 8 greenq 1 0.0 0.0 90.0 10.0/0.0 36 1 363.96 " 
	tstr2 = "super-equil.sh super_relax.py a 0 1 locked_template"
	tstr3 = "super-equil.sh super_relax.py a 0 1 locked_frozen"

	ttxtf = open("tasks.crwl","r")
	ttxt = ttxtf.read()
	ttxtf.close()
        ttxt += header + "\n"
	n=267

        k=1
        ps = 1.011
        sol = 956.0
        
        for ps in np.logspace(np.log10(0.4),1.0,num=20):
            ttxt+=(str(n)+" plasim jadepress"+str(k)+tstr1+str(ps)+" "+str(sol)
                    +" "+tstr2+'\n')
            n+=1
            ttxt+=(str(n)+" plasim cjadepress"+str(k)+tstr1+str(ps)+" "+str(sol)
                    +" "+tstr3+'\n')
            n+=1
            k+=1
            
	ttxtf = open("tasks.crwl","w")
	ttxtf.write(ttxt)
	ttxtf.close()