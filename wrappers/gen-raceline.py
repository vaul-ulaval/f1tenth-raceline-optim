import argparse
import sys
import os

# Python black magic :) Do not move this import statement
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import optimize_globaltraj


parser = argparse.ArgumentParser(
    prog='gen-raceline',
    description='This is a wrapper program to help generate racelines from centerlines generated with the "gen-centerline" wrapper')
parser.add_argument('--track-path', required=True,
                    help='Path to the .csv file generated with the gen-centerline utility')
parser.add_argument(
    '--optim-type', choices=['shortest_path', 'mincurv', 'mincurv_iqp', 'mintime'], default='mintime', help='''
    shortest_path: Shortest path optimization
    mincurv: Minimum curvature optimization without iterative call
    mincurv_iqp: Minimum curvature optimization with iterative call
    mintime: Time-optimal trajectory optimization
''')
args = parser.parse_args()


track_path: str = args.track_path
optim_type: str = args.optim_type

# Argument validation
if not os.path.isfile(track_path):
    print('Error! Track path file not found')
    sys.exit(-1)
if not track_path.endswith('.csv'):
    print('Error! track file must be a .csv file generated with the "gen-centerline" wrapper')
    sys.exit(-1)

optimize_globaltraj.launch_globaltraj_optimization(track_path, 'f110.ini', optim_type)
