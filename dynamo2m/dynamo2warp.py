### Conversion of dynamo format table files into a STAR file for particle extraction in WARP ###
# Requires
#  - dynamotable (depends on pandas)
#  - starfile (depends on pandas)
#  - eulerangles (depends on numpy)
#  - click
# tested and working against warp v1.0.7

import click
import dynamotable
import starfile
import pandas as pd
from eulerangles import euler2euler
from .utils import sanitise_micrograph_name, sanitise_m_starfile_name


@click.command()
@click.option('--input_table_file', '-i',
              prompt='Input Dynamo table file',
              type=click.Path(exists=True),
              required=True)
@click.option('--table_map_file', '-tm',
              prompt='Input Dynamo table map file',
              type=click.Path(exists=True),
              required=True)
@click.option('--output_star_file', '-o',
              prompt='Output STAR file'
              )
def cli(input_table_file, table_map_file, output_star_file):
    # Read table file into dataframe
    click.echo(f"Reading table file '{input_table_file}' and '{table_map_file}'...")
    table = dynamotable.read(input_table_file, table_map_file)

    # Prep data for star file in dict
    data = {}

    # extract xyz into dict with relion style headings
    click.echo(f"Extracting XYZ positions...")
    for axis in ('x', 'y', 'z'):
        heading = f'rlnCoordinate{axis}'
        shift_axis = f'd{axis}'
        data[heading] = table[axis] + table[shift_axis]

    # extract and convert eulerangles
    click.echo(f"Converting euler angles from Dynamo convention to Warp convention...")
    eulers_dynamo = dynamotable.eulers(table)
    eulers_warp = euler2euler(eulers_dynamo, source_convention='dynamo', target_convention='warp')
    data['rlnAngleRot'] = eulers_warp[:, 0]
    data['rlnAngleTilt'] = eulers_warp[:, 1]
    data['rlnAnglePsi'] = eulers_warp[:, 2]

    # extract and sanitise micrograph names to ensure compatibility with M
    click.echo(f"Correcting tomogram names to ensure compatibility with M...")
    data['rlnMicrographName'] = table['tomo_file'].apply(sanitise_micrograph_name)

    # convert dict to dataframe
    df = pd.DataFrame.from_dict(data)

    # Make sure filename is M compatible
    click.echo(f"Making sure STAR filename is compatible with M...")
    output_star_file = sanitise_m_starfile_name(output_star_file)

    # write out STAR file
    click.echo(f"Writing out STAR file with appropriate info...")
    starfile.write(df, output_star_file)

    # echo to console
    click.echo(f"Done! Converted '{input_table_file}' to RELION/Warp compatible STAR file '{output_star_file}'")

    return




