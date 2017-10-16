import edu.bupt.service.DocService as ds
import edu.bupt.service.SegmentService as Segment

if __name__ == '__main__':
    docService = ds.DocService()
    segmentService = Segment.SegmentService()

    sql = 'select docno,title, content from tb_doc'
    result = docService.fetch(sql)

    tmp_columns = []
    i = 0
    column = {}


    for item in result:
        seg_title = segmentService.defaultSegment(item['title'])
        seg_content = segmentService.defaultSegment(item['content'])
        column['seg_title'] = seg_title
        column['seg_content'] = seg_content
        column['docno'] = item['docno']
        tmp_columns.append(column)
        print 'ok: ', i
        i = i + 1
        if len(tmp_columns) == 100:
            docService.insertBatch('tb_segment', tmp_columns)
            tmp_columns = []



            # for item in result:
            #     print item['title']
            # data = [{'id': 1, 'x': 2, 'y': 3}, {'id': 1, 'x': 2, 'y': 3}]
            # docService.insertBatch('map', data)
