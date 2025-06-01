from api_handler import get_by_title, get_by_id, search_by_name
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="OMDB CLI Tool", description="Search or Look for a Movie/Show/Episode from the OMDB")

    # Search values
    parser.add_argument("--search", action="store_true")
    parser.add_argument("--title")
    parser.add_argument("--year", default=None)
    parser.add_argument("--type", default="movie")
    parser.add_argument("--page", default=1)

    # Searchless values

    parser.add_argument("--imdb")
    parser.add_argument("--plot", default="short")

    args = parser.parse_args()

    if args.search:
        try:
            response = search_by_name(
                args.title, args.type, args.year, args.page)

            print("-------------------------------")
            print(response.Title)
            print(
                f"Year: {response.Year}, Runtime: {response.Runtime}, Genre: {response.Genre}")
            print(response.Plot)
            print(
                f"Ratings:\nRotten Tomatoes: {response.Ratings[1].Value}\nMetacritic: {response.Ratings[2].Value}")
            print("-------------------------------")

        except ValueError as e:
            return sys.exit(e)

    else:
        if args.imdb:
            try:
                response = get_by_id(args.imdb, args.year,
                                     args.type,  args.plot)

                print("-------------------------------")
                print(response.Title)
                print(
                    f"Year: {response.Year}, Runtime: {response.Runtime}, Genre: {response.Genre}")
                print(response.Plot)
                print(
                    f"Ratings:\nRotten Tomatoes: {response.Ratings[1].Value}\nMetacritic: {response.Ratings[2].Value}")
                print("-------------------------------")

            except ValueError as e:
                return sys.exit(e)

        else:
            try:
                response = get_by_title(
                    args.title, args.year, args.type, args.plot)

                print("-------------------------------")
                print(response.Title)
                print(
                    f"Year: {response.Year}, Runtime: {response.Runtime}, Genre: {response.Genre}")
                print(response.Plot)
                print(
                    f"Ratings:\nRotten Tomatoes: {response.Ratings[1].Value}\nMetacritic: {response.Ratings[2].Value}")
                print("-------------------------------")

            except ValueError as e:
                return sys.exit(e)


if __name__ == "__main__":
    main()
