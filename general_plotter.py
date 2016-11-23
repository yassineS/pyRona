#!/usr/bin/python3
# Copyright 2016 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of pyRona.
# pyRona is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyRona is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyRona.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt
import numpy as np


def draw_individual_plots(present_covar, future_covar, rona, marker_name,
                          allele_freqs, fit_fn):
    """
    Draws an individual marker vs covar plot.
    """
    all_covars = np.append(present_covar, future_covar)

    # Set-up the plot
    plt.xlabel("Covariate %s" % rona.name)
    plt.ylabel('Marker %s standardized allele freqs.' % marker_name)
    plt.title('Linear regression plot')

    plt.plot(present_covar, allele_freqs, 'bo')
    plt.plot(future_covar, allele_freqs, 'go')
    plt.plot(all_covars, fit_fn(all_covars), 'r--')

    plt.xlim(min(all_covars) - np.average(present_covar) * 0.1,
             max(all_covars) + np.average(present_covar) * 0.1)
    plt.ylim(min(allele_freqs) - min(allele_freqs) * 0.1,
             max(allele_freqs) + max(allele_freqs) * 0.1)


    # Annotation
    for label, x, y in zip(rona.pop_names, present_covar, allele_freqs):
        plt.annotate(label.strip(), xy=(x, y), xytext=(-9, 9),
                     textcoords='offset points', ha='right',
                     va='bottom', bbox=dict(boxstyle='round,pad=0.1',
                                            fc='yellow',
                                            alpha=0.3),
                     arrowprops=dict(arrowstyle='->',
                                     connectionstyle='arc3,rad=0'))

    plt.show()


def draw_rona_plot(rona, units):
    """
    Draws a RONA plot of the Nth most represented covariates.
    Plots the RONA+/-Stderr for each of the populations.
    """
    fig, ax = plt.subplots()
    width = 0.35
    ind = np.arange((len(rona.pop_names)))

    # Set-up the plot
    #plt.xlabel(rona.pop_names)
    #plt.ylabel("RONA value, %s" % rona.count_markers)
    #plt.title("RONA per population for the most represented %s covariates" %
    #          units)

    rects1 = ax.bar(ind, rona.avg_ronas, width,
                    color='r', yerr=rona.stderr_ronas)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('RONA')
    ax.set_title("RONA per population for the most represented %s covariates" %
              units)
    ax.set_xticks(ind + width)
    ax.set_xticklabels((rona.pop_names))


    #plt.plot(range(len(rona.pop_names)), rona.avg_ronas, 'bo')
    #plt.errorbar(range(len(rona.pop_names)), rona.avg_ronas, yerr=rona.stderr_ronas, fmt='bo')
    #plt.plot(range(len(rona.pop_names)), rona.stderr_ronas, '--')

    plt.show()
