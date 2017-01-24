import fiona 
import shapely
import argparse 
import os
import json
import geojson

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Separate parcelles full shapefile in one geojson per feature and store them in ipfs')
    parser.add_argument("shp", help="the path of the shapefile file, ends with .shp")
    parser.add_argument("output_dir", help="the directory where you want to generate splitted parcelles")
    args = parser.parse_args()
    print(args.output_dir)
    print(args.shp)

    if os.path.exists(args.output_dir) and os.path.isdir(args.output_dir):
        print('Warning : The folder already exists, delete it before running the script')
        quit()
    else:
        os.mkdir(args.output_dir)
 
    for pol in fiona.open(args.shp):  

         
        geojson = json.dumps({"type": "Feature", "geometry": pol['geometry'], "properties": pol['properties']}).replace('\\', '').replace('(', '[').replace(')', ']')

        # TODO : fix geom invalidity (maybe OrderedDict todo or something else)
        #valid = geojson.is_valid(geojson)
        #print(valid)

        # TODO : note that projection is 2154

        name = '{}.geojson'.format(pol['properties']['Ident'])
        with open('{output_dir}/{name}'.format(output_dir=args.output_dir, name=name), 'a') as geojson_file:           
            print('Writing {} in filesystem'.format(name))
            geojson_file.write(geojson)
        
