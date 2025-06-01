from api_handler import get_by_title, get_by_id, search_by_name
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
            prog="OMDB CLI Tool", description="Search or Look for a Movie/Show/Episode from the OMDB.", epilog="If --search is given all arguments are valid except --imdb and --plot, if not, all arguments are valid except --page")

    # Search values
    parser.add_argument("--search", action="store_true")
    parser.add_argument("--title")
    parser.add_argument("--year", default=None)
    parser.add_argument("--type", default="movie", choices=["movie", "series", "episode"])
    parser.add_argument("--page", default=1, choices=["Range from 1  to 100"])

    # Searchless values

    parser.add_argument("--imdb", choices=["IMDB ID"])
    parser.add_argument("--plot", default="short", choices=["short", "full"])

    args = parser.parse_args()

    if args.search:
        try:
            response = search_by_name(
                args.title, args.type, args.year, int(args.page))

                           
            print("-------------------------------")
            for n in range(0, len(response['Search'])):
                print(
                    f"{n+1}. {response['Search'][n]['Title']}\nYear: {response['Search'][n]['Year']}\nIMDB Id: {response['Search'][n]['imdbID']}")

            print("-------------------------------")

        except ValueError as e:
            return sys.exit(e)
        except KeyError:
            return sys.exit("No results for that search were found")


    else:
        if args.imdb:
            try:
                response = get_by_id(args.imdb, args.year,
                                     args.type,  args.plot)

                print("-------------------------------")
                print(response['Title'])
                print(
                    f"Year: {response['Year']}, Runtime: {response['Runtime']}, Genre: {response['Genre']}")
                print(response['Plot'])

                if args.type == "series":
                    print(f"Ratings:\n\tOpen Movie Database: {response['Ratings'][0]['Value']}")
                elif args.type == "movie":
                    print(
                    f"Ratings:\n\tRotten Tomatoes: {response['Ratings'][1]['Value']}\n\tMetacritic: {response['Ratings'][2]['Value']}")

                print("-------------------------------")

            except ValueError as e:
                return sys.exit(e)

            except KeyError:
                return sys.exit(f"No {args.type} was found")

        else:
            try:
                response = get_by_title(
                    args.title, args.year, args.type, args.plot)

                print("-------------------------------")
                print(response['Title'])
                print(
                    f"Year: {response['Year']}, Runtime: {response['Runtime']}, Genre: {response['Genre']}")
                print(response['Plot'])
                if args.type == "series":
                    print(f"Ratings:\n\tOpen Movie Database: {response['Ratings'][0]['Value']}")
                elif args.type == "movie":
                    print(
                    f"Ratings:\n\tRotten Tomatoes: {response['Ratings'][1]['Value']}\n\tMetacritic: {response['Ratings'][2]['Value']}")
                print("-------------------------------")

            except ValueError as e:
                return sys.exit(e)

            except KeyError:
                return sys.exit(f"No {args.type} was found")


if __name__ == "__main__":
    main()
