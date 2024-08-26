import sys, os, argparse


class recommender:
    pass

def get_args():
    parser = argparse.ArgumentParser(description="Anime recommender system")
    # parser.add_argument("-t", "--title", action="store", type=str, 
    #                     help="Recommends anime based on given title.")
    
    parser.add_argument("id", action="store", type=str, 
                        help="returns recommended anime titles based on given anime_id.") 
    parser.add_argument("-c", "--count", action='store', type=int, default=10,
                        help="Number of titles to be recommended.")

    args = parser.parse_args()
    return args
    

if __name__ == "__main__":
    
    args = get_args()
    print(args.id)

    

else:
    pass