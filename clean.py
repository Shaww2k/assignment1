import pandas as pd


def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df_temp = df1.merge(df2, left_on='respondent_id', right_on='id').dropna()
    df = df_temp[df_temp['job'].str.contains('insurance' or 'Insurance') == False]
    df = df.drop('id', axis=1)
    print("the shape of output dataframe", df.shape)
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file, args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)
