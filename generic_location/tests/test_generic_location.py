from odoo.tests.common import TransactionCase


class TestGenericLocation(TransactionCase):

    def test_create_location(self):
        simplelocation = self.env.ref(
            'generic_location.' 'simple_parent_location_4')
        self.assertNotEqual(simplelocation.name, simplelocation.copy().name)
        self.assertEqual(simplelocation.name, 'Hostel-3')
        self.assertEqual(simplelocation.child_ids.name, 'Room 9')
        self.assertEqual(simplelocation.child_count, 1)
        # Test action button
        testaction = simplelocation.action_button_show_sublocations()
        self.assertEqual(testaction['name'], 'Sublocations')
        self.assertEqual(testaction['res_model'], simplelocation._name)
        testdomain = testaction['domain']
        self.assertEqual(testdomain[0], ('parent_id', '=', simplelocation.id))

    def test_location_parent_names(self):
        root = self.env['generic.location'].create({
            'name': 'Root',
        })
        child = self.env['generic.location'].create({
            'name': 'Child',
            'parent_id': root.id,
        })
        self.assertEqual(child.display_name, 'Root / Child')
