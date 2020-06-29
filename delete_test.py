import cx_Oracle
# import config as cfg


def delete_billing(billing_no, amount):
    """
    Delete a billing based on a billing no.
    :param billing_no:
    :return:
    """
    sql = 'DELETE FROM DOAN3.GIANG_VIEN WHERE ID_GV =:112233'
    try:
        # establish a new connection
        with cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [amount, billing_no])
                # commit the change
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)


# if __name__ == '__main__':
#     delete_billing(1)