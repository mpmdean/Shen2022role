import numpy as np
import matplotlib.pyplot as plt

def calc_Elevels(Deg=0., Dt2g=0., tenDq=0., Dsp=0.5, Dpa=0., Dzp=0., dp=0., Delta=5.8,
                 Tpp=0.75, Vpd_sigma=1.55, sign=1, ax=None):
    
    color_table = dict(p_sigma='C3', p_pi='C0', p_z='C2')
    text_params = dict(fontdict=dict(fontsize=6), rotation=90, horizontalalignment='center')
    
    ### calculate energy levels
    ## before hyb
    p_orbs = dict(p_sigma=dp, p_pi=dp+Dsp, p_z=dp+Dsp)
    ## after in-plane pp hyb
    p_orbs_pp = dict(p_sigma_B=dict(value=p_orbs['p_sigma']+Tpp, pre='p_sigma', cata='p_sigma'),
                     p_sigma_AB=dict(value=p_orbs['p_sigma']-Tpp, pre='p_sigma', cata='p_sigma'),
                     p_pi_B=dict(value=p_orbs['p_pi']+Tpp, pre='p_pi', cata='p_pi'),
                     p_pi_AB=dict(value=p_orbs['p_pi']-Tpp, pre='p_pi', cata='p_pi'),
                     p_z_NB=dict(value=p_orbs['p_z'], pre='p_z', cata='p_z'))
    ## after pd hyb
    p_orbs_pd = dict(p_pi_AB=dict(value=p_orbs_pp['p_pi_AB']['value'], pre='p_pi_AB', cata='p_pi'))
    # planar p_sigma
    emat = [[-Delta+Deg+dp, Vpd_sigma],
            [Vpd_sigma, p_orbs_pp['p_sigma_B']['value']]]
    evals, _ = np.linalg.eigh(emat)
    p_orbs_pd['p_sigma_B'] = dict(value=evals[1], pre='p_sigma_B', cata='p_sigma')
    # planar p_z
    emat = [[-Delta+tenDq+Dt2g+dp, Vpd_sigma / np.sqrt(2)],
            [Vpd_sigma / np.sqrt(2), p_orbs_pp['p_z_NB']['value']]]
    evals, _ = np.linalg.eigh(emat)
    p_orbs_pd['p_z_NB'] = dict(value=evals[1], pre='p_z_NB', cata='p_z')
    # planar p_sigma
    emat = [[-Delta+dp, np.sqrt(3) * Vpd_sigma],
            [np.sqrt(3) * Vpd_sigma, p_orbs_pp['p_sigma_AB']['value']]]
    evals, _ = np.linalg.eigh(emat)
    p_orbs_pd['p_sigma_AB'] = dict(value=evals[1], pre='p_sigma_AB', cata='p_sigma')
    # planar p_pi
    emat = [[-Delta+tenDq+dp, Vpd_sigma],
            [Vpd_sigma, p_orbs_pp['p_pi_B']['value']]]
    evals, _ = np.linalg.eigh(emat)
    p_orbs_pd['p_pi_B'] = dict(value=evals[1], pre='p_pi_B', cata='p_pi')

    ### plot the results
    if ax is None:
        fig, ax = plt.subplots()
    ## before hyb
    Es = [1e3]
    for orb_key in p_orbs.keys():
        x = sign * np.array([0., 1.])
        y = [p_orbs[orb_key], p_orbs[orb_key]]
        if np.min(abs(y[0]-np.array(Es)))<1e-5:
            ax.plot(x, y, ':', color=color_table[orb_key], lw=1)
        else:
            ax.plot(x, y, '-', color=color_table[orb_key], lw=1)
            Es.append(y[0])
    ax.text(sign*0.5, np.max(Es[1:])+0.3, r'without hopping', **text_params)
    ## after in-plane pp hyb
    Es = [1e3]
    for orb_key in p_orbs_pp.keys():
        x = sign * np.array([1., 1.4])
        y = [p_orbs[p_orbs_pp[orb_key]['pre']], p_orbs_pp[orb_key]['value']]
        ax.plot(x, y, ':', color='grey', lw=0.5)
        x = sign * np.array([1.4, 2.4])
        y = [p_orbs_pp[orb_key]['value'], p_orbs_pp[orb_key]['value']]
        if np.min(abs(y[0]-np.array(Es)))<1e-5:
            ax.plot(x, y, ':', color=color_table[p_orbs_pp[orb_key]['cata']], lw=1)
        else:
            ax.plot(x, y, '-', color=color_table[p_orbs_pp[orb_key]['cata']], lw=1)
            Es.append(y[0])
    ax.text(sign*1.9, np.max(Es[1:])+0.3, r'$pp$ hopping', **text_params)
    ## after pd hyb
    Es = [1e3]
    for orb_key in p_orbs_pd.keys():
        x = sign * np.array([2.4, 2.8])
        y = [p_orbs_pp[p_orbs_pd[orb_key]['pre']]['value'], p_orbs_pd[orb_key]['value']]
        ax.plot(x, y, ':', color='grey', lw=0.5)
        x = sign * np.array([2.8, 3.8])
        y = [p_orbs_pd[orb_key]['value'], p_orbs_pd[orb_key]['value']]
        if np.min(abs(y[0]-np.array(Es)))<1e-5:
            ax.plot(x, y, ':', color=color_table[p_orbs_pd[orb_key]['cata']], lw=1)
        else:
            ax.plot(x, y, '-', color=color_table[p_orbs_pd[orb_key]['cata']], lw=1)
            Es.append(y[0])
    ax.text(sign*3.3, np.max(Es[1:])+0.3, r'$pd$ hopping', **text_params)